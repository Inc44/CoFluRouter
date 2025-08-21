import json
import requests
from pathlib import Path

from data import OPENAI_COMPATIBLE


def redact_keys(obj, keys):
	if isinstance(obj, dict):
		return {
			key: (0 if key in keys else redact_keys(value, keys))
			for key, value in obj.items()
		}
	if isinstance(obj, list):
		return [redact_keys(value, keys) for value in obj]
	return obj


def redact_entry(obj, entry, prefix):
	if isinstance(obj, dict):
		return {key: redact_entry(value, entry, prefix) for key, value in obj.items()}
	if isinstance(obj, list):
		return [
			redact_entry(value, entry, prefix)
			for value in obj
			if not (
				isinstance(value, dict)
				and isinstance(value.get(entry), str)
				and value.get(entry).startswith(prefix)
			)
		]
	return obj


def sort_by_id(obj):
	if isinstance(obj, dict) and isinstance(obj.get("data"), list):
		obj["data"].sort(
			key=lambda value: value.get("id", "") if isinstance(value, dict) else ""
		)
	elif isinstance(obj, list):
		obj.sort(
			key=lambda value: value.get("id", "") if isinstance(value, dict) else ""
		)


for name, base_url, api_key in OPENAI_COMPATIBLE:
	if name in ["Minimax", "Perplexity"]:
		continue
	models = "models"
	headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
	if name == "Anthropic":
		models = "v1/models"
		headers = {
			"x-api-key": api_key,
			"anthropic-version": "2023-06-01",
			"Accept": "application/json",
		}
	url = base_url + "/" + models
	resp = requests.get(url, headers=headers)
	obj = resp.json()
	if name in ["Chutes", "Hyperbolic"]:
		obj = redact_keys(obj, {"created"})
	if name == "Chutes":
		obj = redact_keys(obj, {"tao"})
		obj = redact_entry(obj, "id", "modelperm-")
	if name == "OpenAI":
		obj = redact_entry(obj, "id", "ft:")
	sort_by_id(obj)
	path = Path(f"models/external/{name}.json")
	path.parent.mkdir(parents=True, exist_ok=True)
	path.write_text(
		json.dumps(obj, indent="\t", sort_keys=True, ensure_ascii=False),
		encoding="utf-8",
	)
	if "data" in obj:
		models = [model["id"] for model in obj["data"]]
	else:
		models = [model["id"] for model in obj]
	for model in models:
		print(f"{name}: {model}", file=open("lists/list2.txt", "a"))
