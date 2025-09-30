import json
from pathlib import Path

from categorizer import list_high_cost_models
from data import OPENAI_COMPATIBLE


def extract_max_tokens(item):
	max_tokens = item.get("max_completion_tokens")
	if (
		not max_tokens
		and "metadata" in item
		and item["metadata"] is not None
		and item["metadata"].get("max_tokens")
	):
		max_tokens = item["metadata"]["max_tokens"]
	if (
		not max_tokens
		and "top_provider" in item
		and item["top_provider"].get("max_completion_tokens")
	):
		max_tokens = item["top_provider"]["max_completion_tokens"]
	return max_tokens


def extract_image_support(item):
	if "architecture" in item:
		architecture = item["architecture"]
		if (
			"input_modalities" in architecture
			and "image" in architecture["input_modalities"]
		):
			return True
		if "modality" in architecture and "image" in architecture["modality"]:
			return True
	if "pricing" in item and "image" in item["pricing"]:
		return True
	if "input_modalities" in item and "image" in str(item["input_modalities"]):
		return True
	if (
		"metadata" in item
		and item["metadata"] is not None
		and "tags" in item["metadata"]
		and "vision" in item["metadata"]["tags"]
	):
		return True
	if item.get("supports_image_input"):
		return True
	return False


def extract_audio_support(item):
	if (
		"architecture" in item
		and "input_modalities" in item["architecture"]
		and "audio" in item["architecture"]["input_modalities"]
	):
		return True
	if "pricing" in item and "audio" in item["pricing"]:
		return True
	return False


def skip_model(item):
	if "supports_chat" in item and not item.get("supports_chat"):
		return True
	if "type" in item and "image" in item["type"]:
		return True
	if "id" in item and (
		"flux" in str(item["id"]).lower()
		or "sdxl" in str(item["id"]).lower()
		or (
			"stable" in str(item["id"]).lower()
			and "diffusion" in str(item["id"]).lower()
		)
	):
		return True
	return False


def is_transcription_model(item):
	if "type" in item and "transcribe" in item["type"]:
		return True
	if "pricing" in item and "duration_per_hour" in item["pricing"]:
		return True
	if "max_completion_tokens" in item and item["max_completion_tokens"] == 448:
		return True
	if "id" in item and (
		"transcribe" in str(item["id"]).lower() or "whisper" in str(item["id"]).lower()
	):
		return True
	return False


def list_models():
	high_cost_models = list_high_cost_models()
	models = []
	for name, _, _ in OPENAI_COMPATIBLE:
		if name in ["Minimax", "Perplexity"]:
			continue
		path = Path(f"models/external/{name}.json")
		path.parent.mkdir(parents=True, exist_ok=True)
		obj = json.loads(path.read_text(encoding="utf-8"))
		if "data" in obj:
			obj = obj["data"]
		for item in obj:
			if skip_model(item):
				continue
			model = {}
			model["name"] = name
			if "id" in item and item["id"].split("/")[-1].lower() in high_cost_models:
				model["high_cost"] = True
			if is_transcription_model(item):
				model["transcription"] = True
			if "id" in item:
				model["id"] = item["id"].split("/")[-1].lower()
			max_tokens = extract_max_tokens(item)
			if max_tokens:
				model["max_tokens"] = max_tokens
			model["image"] = extract_image_support(item)
			audio = extract_audio_support(item)
			if audio:
				model["audio"] = audio
			models.append(model)
	models.sort(key=lambda model: model["name"] + model["id"])
	return models
