import json
from pathlib import Path

from data import OPENAI_COMPATIBLE


def list_high_cost_models():
	models = []
	for name, _, _ in OPENAI_COMPATIBLE:
		if name in ["Minimax", "Perplexity"]:
			continue
		path = Path(f"models/external/{name}.json")
		path.parent.mkdir(parents=True, exist_ok=True)
		obj = json.loads(path.read_text(encoding="utf-8"))
		threshold = 15
		if name == "OpenRouter":
			threshold /= 1_000_000
		if "data" in obj:
			obj = obj["data"]
		models.extend(
			[
				str(model["id"]).split("/")[-1].lower().replace(".", "-")
				for model in obj
				if model.get("pricing", {})
				and any(
					(
						float(price) >= threshold
						if price_key not in ["duration_per_hour", "image", "web_search"]
						else False
					)
					for price_key, price in model["pricing"].items()
				)
			]
		)
	models.sort()
	return models
