from pathlib import Path
from utils import read_json, write_json

source_dir = Path("models/external")
target_dirs = [
	Path("models/completion"),
	Path("models/completion.high.cost"),
	Path("models/transcription"),
]
for source_path in source_dir.glob("*.json"):
	ext_obj = read_json(source_path)
	if "data" in ext_obj:
		ext_obj = ext_obj["data"]
	if ext_obj is None:
		continue
	models = [
		str(model["id"])
		for model in ext_obj
		if isinstance(model, dict) and "id" in model
	]
	index_map = {model_id: i for i, model_id in enumerate(models)}
	sentinel = len(models) + 999
	name = source_path.stem
	for target_dir in target_dirs:
		target_path = target_dir / f"{name}.json"
		if not target_path.exists():
			continue
		obj = read_json(target_path)
		if "data" in obj:
			obj = obj["data"]
		if obj is None:
			continue
		sorted_models = sorted(
			obj,
			key=lambda model: index_map.get(
				str(model.get("id")) if isinstance(model, dict) else None, sentinel
			),
		)
		write_json(target_path, {"data": sorted_models})
