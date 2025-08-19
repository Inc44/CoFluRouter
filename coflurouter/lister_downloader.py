import json
import requests
from pathlib import Path

from data import OPENAI_COMPATIBLE

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
	path = Path(f"downloads/{name}.json")
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
