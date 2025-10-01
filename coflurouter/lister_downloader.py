from pathlib import Path

import requests

from data import OPENAI_COMPATIBLE
from utils import read_json, write_json


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


def sort_by_keys(obj, keys, reverse=False):
	if "data" in obj:
		obj = obj["data"]
	if isinstance(obj, list):
		obj.sort(
			key=lambda value: tuple(
				value.get(key, "") if isinstance(value, dict) else "" for key in keys
			),
			reverse=reverse,
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
	path = Path(f"models/external/{name}.json")
	path.parent.mkdir(parents=True, exist_ok=True)
	obj = resp.json()  # read_json(path) # Testing with fetched models
	if name in ["Chutes", "Hyperbolic"]:  # Redact fetch time
		obj = redact_keys(obj, {"created"})
	if name == "Chutes":  # Redact crypto, pricing and permissions
		obj = redact_keys(obj, {"completion"})
		obj = redact_keys(obj, {"prompt"})
		obj = redact_keys(obj, {"tao"})
		obj = redact_keys(obj, {"usd"})
		obj = redact_entry(obj, "id", "modelperm-")
	if name == "OpenAI":  # Redact fine-tuned models
		obj = redact_entry(obj, "id", "ft:")
	if name in [
		"Anthropic",
		"Cerebras",
		"Chutes",
		"DeepInfra",
		"Google",
		"Groq",
		"Hyperbolic",
		"Lambda",
	]:  # Sort random order models
		sort_by_keys(obj, ["id"])
	# Sort by latest models
	if name == "Anthropic":
		sort_by_keys(obj, ["created_at", "name"], reverse=True)
	else:
		sort_by_keys(obj, ["created", "name"], reverse=True)
	write_json(path, obj, True)
	if "data" in obj:
		obj = obj["data"]
	models = [model["id"] for model in obj]
	for model in models:
		print(f"{name}: {model}", file=open("lists/list2.txt", "a"))
