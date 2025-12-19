# CoFluRouter

![Stars](https://img.shields.io/github/stars/Inc44/CoFluRouter?style=social)
![Forks](https://img.shields.io/github/forks/Inc44/CoFluRouter?style=social)
![Watchers](https://img.shields.io/github/watchers/Inc44/CoFluRouter?style=social)
![Repo Size](https://img.shields.io/github/repo-size/Inc44/CoFluRouter)
![Language Count](https://img.shields.io/github/languages/count/Inc44/CoFluRouter)
![Top Language](https://img.shields.io/github/languages/top/Inc44/CoFluRouter)
[![Issues](https://img.shields.io/github/issues/Inc44/CoFluRouter)](https://github.com/Inc44/CoFluRouter/issues?q=is%3Aopen+is%3Aissue)
![Last Commit](https://img.shields.io/github/last-commit/Inc44/CoFluRouter?color=red)
[![Release](https://img.shields.io/github/release/Inc44/CoFluRouter.svg)](https://github.com/Inc44/CoFluRouter/releases)
[![Sponsor](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/Inc44)

CoFluRouter CLI

## ⚠️ Disclaimers

- **Deprecated Models**: The goal of this project is to archive models; therefore, some models may no longer be available.
- **Missing Models**: This project was created after some models were deprecated; therefore, some may be missing. For example:

| Name                  | ID                       | Created     | Context Length | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------|--------------------------|-------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Horizon Beta          | openrouter/horizon-beta  | 2025 Aug 1  | 256000         | This is a cloaked model provided to the community to gather feedback. This is an improved version of [Horizon Alpha](https://openrouter.ai/openrouter/horizon-alpha)<br>Note: It’s free to use during this testing period, and prompts and completions are logged by the model creator for feedback and training.                                                                                                                                                                                                                                       |
| Horizon Alpha         | openrouter/horizon-alpha | 2025 Jul 30 | 256000         | This was a cloaked model provided to the community to gather feedback. It has been deprecated - see [Horizon Beta](https://openrouter.ai/openrouter/horizon-beta).<br>Note: It’s free to use during this testing period, and prompts and completions are logged by the model creator for feedback and training.                                                                                                                                                                                                                                         |
| Cypher Alpha          | openrouter/cypher-alpha  | 2025 Jul 1  | 1000000        | This is a cloaked model provided to the community to gather feedback. It's an all-purpose model supporting real-world, long-context tasks including code generation.<br>Note: All prompts and completions for this model are logged by the provider and may be used to improve the model and other products and services. You remain responsible for any required end user notices and consents and for ensuring that no personal, confidential, or otherwise sensitive information, including data from individuals under the age of 18, is submitted. |
| Optimus Alpha         | openrouter/optimus-alpha | 2025 Apr 10 | 1000000        | This is a cloaked model provided to the community to gather feedback. It's geared toward real world use cases, including programming.<br>Note: All prompts and completions for this model are logged by the provider and may be used to improve the model.                                                                                                                                                                                                                                                                                              |
| Quasar Alpha          | openrouter/quasar-alpha  | 2025 Apr 2  | 1000000        | This is a cloaked model provided to the community to gather feedback. It’s a powerful, all-purpose model supporting long-context tasks, including code generation.<br>Note: All prompts and completions for this model are logged by the provider  and may be used to improve the model.                                                                                                                                                                                                                                                                |
| Cinematika 7B (alpha) | openrouter/cinematika-7b | 2023 Dec 6  | 8000           | This model is under development. Check the [OpenRouter Discord](https://discord.gg/fVyRaUDgxW) for updates.                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## 🚀 Installation

```bash
conda create -n coflurouter python=3.10 -y # up to 3.13
conda activate coflurouter
git clone https://github.com/Inc44/CoFluRouter.git
cd CoFluRouter
pip install -r requirements.txt
```

## 🧾 Configuration

Set environment variable:

```powershell
setx /M CEREBRAS_API_KEY your_api_key
setx /M OPENAI_API_KEY your_api_key
setx /M CHUTES_API_KEY your_api_key
setx /M ANTHROPIC_API_KEY your_api_key
setx /M DEEPINFRA_API_KEY your_api_key
setx /M DEEPSEEK_API_KEY your_api_key
setx /M GOOGLE_API_KEY your_api_key
setx /M X_API_KEY your_api_key
setx /M GROQ_API_KEY your_api_key
setx /M HYPERBOLIC_API_KEY your_api_key
setx /M LAMBDA_API_KEY your_api_key
setx /M MINIMAX_API_KEY your_api_key
setx /M OPENROUTER_API_KEY your_api_key
setx /M PERPLEXITY_API_KEY your_api_key
setx /M ALIBABA_API_KEY your_api_key
setx /M SAMBANOVA_API_KEY your_api_key
setx /M TOGETHER_API_KEY your_api_key
```

For Linux/macOS:

```bash
echo 'export CEREBRAS_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export OPENAI_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export CHUTES_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export ANTHROPIC_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export DEEPINFRA_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export DEEPSEEK_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export GOOGLE_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export X_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export GROQ_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export HYPERBOLIC_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export LAMBDA_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export MINIMAX_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export OPENROUTER_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export PERPLEXITY_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export ALIBABA_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export SAMBANOVA_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
echo 'export TOGETHER_API_KEY="your_api_key"' >> ~/.bashrc # or ~/.zshrc
```

Or create a `.env` file or modify /etc/environment:

```
CEREBRAS_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
CHUTES_API_KEY=your_api_key
ANTHROPIC_API_KEY=your_api_key
DEEPINFRA_API_KEY=your_api_key
DEEPSEEK_API_KEY=your_api_key
GOOGLE_API_KEY=your_api_key
X_API_KEY=your_api_key
GROQ_API_KEY=your_api_key
HYPERBOLIC_API_KEY=your_api_key
LAMBDA_API_KEY=your_api_key
MINIMAX_API_KEY=your_api_key
OPENROUTER_API_KEY=your_api_key
PERPLEXITY_API_KEY=your_api_key
ALIBABA_API_KEY=your_api_key
SAMBANOVA_API_KEY=your_api_key
TOGETHER_API_KEY=your_api_key
```

Check by restarting the terminal and using:

```cmd
echo %CEREBRAS_API_KEY%
echo %OPENAI_API_KEY%
echo %CHUTES_API_KEY%
echo %ANTHROPIC_API_KEY%
echo %DEEPINFRA_API_KEY%
echo %DEEPSEEK_API_KEY%
echo %GOOGLE_API_KEY%
echo %X_API_KEY%
echo %GROQ_API_KEY%
echo %HYPERBOLIC_API_KEY%
echo %LAMBDA_API_KEY%
echo %MINIMAX_API_KEY%
echo %OPENROUTER_API_KEY%
echo %PERPLEXITY_API_KEY%
echo %ALIBABA_API_KEY%
echo %SAMBANOVA_API_KEY%
echo %TOGETHER_API_KEY%
```

For Linux/macOS:

```bash
echo $CEREBRAS_API_KEY
echo $OPENAI_API_KEY
echo $CHUTES_API_KEY
echo $ANTHROPIC_API_KEY
echo $DEEPINFRA_API_KEY
echo $DEEPSEEK_API_KEY
echo $GOOGLE_API_KEY
echo $X_API_KEY
echo $GROQ_API_KEY
echo $HYPERBOLIC_API_KEY
echo $LAMBDA_API_KEY
echo $MINIMAX_API_KEY
echo $OPENROUTER_API_KEY
echo $PERPLEXITY_API_KEY
echo $ALIBABA_API_KEY
echo $SAMBANOVA_API_KEY
echo $TOGETHER_API_KEY
```

## 📖 Usage Examples

### Convert Colors to WCAG-Compliant High-Contrast Alternatives

Convert colors to WCAG-compliant high-contrast alternatives:

```bash
python -m coflurouter.cli -a "(255, 0, 0), (0, 255, 0), (0, 0, 255)"
```

### Download External Models Lists

Download `external` models lists:

```bash
python -m coflurouter.cli -f
```

### Update Models Lists

Update `completion`, `completion.high.cost`, `transcription` models lists:

```bash
python -m coflurouter.cli -u
```

## 🎨 Command-Line Arguments

| Argument                              | Description                                                                                |
|---------------------------------------|--------------------------------------------------------------------------------------------|
| `-a, --accessibility [ACCESSIBILITY]` | Convert colors to WCAG-compliant high-contrast alternatives. Format: (r,g,b), (r,g,b), ... |
| `-f, --fetch`                         | Download external models lists.                                                            |
| `-u, --update`                        | Update models lists.                                                                       |

## 🎯 Motivation

Maintaining up-to-date lists of LLM models across dozens of providers is tedious and error-prone. Providers frequently add, deprecate, or rename models. CoFluRouter automates the discovery and configuration process, ensuring that downstream applications have access to accurate pricing, capability flags, and model IDs with minimal manual intervention.

## 🐛 Bugs

Not yet found.

## ⛔ Known Limitations

Not yet known.

## 🚧 TODO

- [ ] [https://api.anthropic.com/v1/messages](json/endpoints/anthropic.messages.json)
- [ ] [https://api.openai.com/v1/chat/completions](json/endpoints/openai.completions.json)
- [ ] [https://api.openai.com/v1/responses](json/endpoints/openai.responses.json)
- [ ] [https://generativelanguage.googleapis.com/v1beta/models](json/endpoints/googleapis.models.json)
- [ ] [https://generativelanguage.googleapis.com/v1beta/openai/chat/completions](json/endpoints/googleapis.completions.json)

## 🙏 Thanks

Creators of:

- [Python](https://www.python.org)
- [Requests](https://requests.readthedocs.io)
- [js-beautify](https://beautifier.io)
- [tqdm](https://tqdm.github.io)

## 🤝 Contribution

Contributions, suggestions, and new ideas are heartily welcomed. If you're considering significant modifications, please initiate an issue for discussion before submitting a pull request.

## 📜 License

[![MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 💖 Support

[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/xamituchido)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/inc44)
[![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/Inc44)