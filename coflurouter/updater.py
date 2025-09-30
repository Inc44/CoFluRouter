from pathlib import Path

from parser import list_models
from utils import read_json, write_json

models = list_models()

for model in models:
	path = Path(f"models/completion/{model['name']}.json")
	if model.get("high_cost"):
		path = Path(f"models/completion.high.cost/{model['name']}.json")
	if model.get("transcription"):
		path = Path(f"models/transcription/{model['name']}.json")
	path.parent.mkdir(parents=True, exist_ok=True)
	if path.exists():
		obj = read_json(path)
	else:
		obj = {"data": []}
	if "data" not in obj or not isinstance(obj["data"], list):
		obj["data"] = obj if isinstance(obj, list) else []
	existing_model = None
	for existing in obj.get("data", []):
		if existing.get("id") == model.get("id"):
			existing_model = existing
			break
	if existing_model:
		if model.get("transcription"):
			existing_model["id"] = model["id"]
		else:
			for key in model:
				if key not in ["name", "high_cost", "transcription"]:
					existing_model[key] = model[key]
	else:
		new_model = {}
		for key in model:
			if key not in ["name", "high_cost", "transcription"]:
				new_model[key] = model[key]
		obj["data"].append(new_model)
	write_json(path, obj)
