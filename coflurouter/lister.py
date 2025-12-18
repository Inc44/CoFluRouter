from __future__ import annotations

from anthropic import Anthropic
from openai import OpenAI
from together import Together

from .data import OPENAI_COMPATIBLE


def list_models():
	for name, base_url, api_key in OPENAI_COMPATIBLE:
		if name in ["Minimax", "Perplexity"]:
			continue
		client = OpenAI(base_url=base_url, api_key=api_key)
		if name == "Anthropic":
			client = Anthropic(base_url=base_url, api_key=api_key)
		if name == "Together":
			client = Together(base_url=base_url, api_key=api_key)
		models = client.models.list()
		for model in models:
			print(f"{name}: {model.id}", file=open("lists/list1.txt", "a"))


if __name__ == "__main__":
	list_models()
