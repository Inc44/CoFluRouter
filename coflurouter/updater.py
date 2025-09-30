import json
from pathlib import Path

import jsbeautifier

from parser import list_models

models = list_models()

for model in models:
	path = Path(f"models/completion/{model['name']}.json")
	if model.get("high_cost"):
		path = Path(f"models/completion.high.cost/{model['name']}.json")
	if model.get("transcription"):
		path = Path(f"models/transcription/{model['name']}.json")
	path.parent.mkdir(parents=True, exist_ok=True)
	if path.exists():
		obj = json.loads(path.read_text(encoding="utf-8"))
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
	opts = {
		"brace_style": "expand",
		"break_chained_methods": True,
		"comma_first": False,
		"e4x": False,
		"end_with_newline": False,
		"indent_char": "\t",
		"indent_empty_lines": False,
		"indent_inner_html": False,
		"indent_scripts": "normal",
		"indent_size": 1,
		"jslint_happy": False,
		"keep_array_indentation": False,
		"max_preserve_newlines": -1,
		"preserve_newlines": False,
		"space_before_conditional": True,
		"unescape_strings": False,
		"wrap_line_length": 0,
	}
	path.write_text(
		jsbeautifier.beautify(json.dumps(obj, indent="\t", ensure_ascii=False), opts),
		encoding="utf-8",
	)
