from __future__ import annotations
import argparse

from .accessibility import accessibility_colors
from .config import Config
from .fetcher import fetch_models
from .updater import update_models


def run(config: Config) -> None:
	if config.accessibility:
		accessibility_colors(config.accessibility)
	if config.fetch:
		fetch_models()
	if config.update:
		update_models()


def main() -> None:
	arg_parser = argparse.ArgumentParser(description="CoFluRouter CLI")
	arg_parser.add_argument(
		"-a",
		"--accessibility",
		type=str,
		nargs="?",
		const="(237, 53, 36), (250, 157, 1), (46, 218, 119), (20, 199, 222), (1, 111, 255), (68, 79, 173), (140, 84, 208)",
		default=None,
		help="Convert colors to WCAG compliant high-contrast alternatives. Format: (r,g,b), (r,g,b), ...",
	)
	arg_parser.add_argument(
		"-f",
		"--fetch",
		action="store_true",
		default=False,
		help="Download external models lists.",
	)
	arg_parser.add_argument(
		"-u",
		"--update",
		action="store_true",
		default=False,
		help="Update models lists.",
	)
	args = arg_parser.parse_args()
	if not (args.accessibility or args.fetch or args.update):
		arg_parser.print_help()
		return
	config = Config(args)
	run(config)


if __name__ == "__main__":
	main()
