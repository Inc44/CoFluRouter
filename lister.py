import json
import os

from anthropic import Anthropic
from dotenv import load_dotenv
from openai import OpenAI
from together import Together

load_dotenv()

OPENAI_COMPATIBLE = [
	(
		"Cerebras",
		"https://api.cerebras.ai/v1",
		os.getenv("CEREBRAS_API_KEY"),
	),
	(
		"OpenAI",
		"https://api.openai.com/v1",
		os.getenv("OPENAI_API_KEY"),
	),
	(
		"Chutes",
		"https://llm.chutes.ai/v1",
		os.getenv("CHUTES_API_KEY"),
	),
	(
		"Anthropic",
		"https://api.anthropic.com",
		os.getenv("ANTHROPIC_API_KEY"),
	),
	(
		"DeepInfra",
		"https://api.deepinfra.com/v1/openai",
		os.getenv("DEEPINFRA_API_KEY"),
	),
	(
		"DeepSeek",
		"https://api.deepseek.com",
		os.getenv("DEEPSEEK_API_KEY"),
	),
	(
		"Google",
		"https://generativelanguage.googleapis.com/v1beta/openai",
		os.getenv("GOOGLE_API_KEY"),
	),
	(
		"X",
		"https://api.x.ai/v1",
		os.getenv("X_API_KEY"),
	),
	(
		"Groq",
		"https://api.groq.com/openai/v1",
		os.getenv("GROQ_API_KEY"),
	),
	(
		"Hyperbolic",
		"https://api.hyperbolic.xyz/v1",
		os.getenv("HYPERBOLIC_API_KEY"),
	),
	(
		"Lambda",
		"https://api.lambdalabs.com/v1",
		os.getenv("LAMBDA_API_KEY"),
	),
	(
		"Minimax",
		"https://api.minimax.io/v1",
		os.getenv("MINIMAX_API_KEY"),
	),
	(
		"OpenRouter",
		"https://openrouter.ai/api/v1",
		os.getenv("OPENROUTER_API_KEY"),
	),
	(
		"Perplexity",
		"https://api.perplexity.ai",
		os.getenv("PERPLEXITY_API_KEY"),
	),
	(
		"Alibaba",
		"https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
		os.getenv("ALIBABA_API_KEY"),
	),
	(
		"SambaNova",
		"https://api.sambanova.ai/v1",
		os.getenv("SAMBANOVA_API_KEY"),
	),
	(
		"Together",
		"https://api.together.xyz/v1",
		os.getenv("TOGETHER_API_KEY"),
	),
]

for name, base_url, api_key in OPENAI_COMPATIBLE:
	if name in ["Minimax", "Perplexity"]:
		continue
	client = OpenAI(base_url=base_url, api_key=api_key)
	if name == "Anthropic":
		client = Anthropic(base_url=base_url, api_key=api_key)
	if name == "Together":
		client = Together(base_url=base_url, api_key=api_key)
	models = client.models.list()
	json.dumps(models)
	for model in models:
		print(f"{name}: {model.id}")
