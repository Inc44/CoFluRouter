from __future__ import annotations
from pathlib import Path
import json
import re

import jsbeautifier


def read_json(path: Path) -> dict:
	return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj: dict, sort_keys: bool = False) -> None:
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
	text = jsbeautifier.beautify(
		json.dumps(obj, indent="\t", sort_keys=sort_keys, ensure_ascii=False), opts
	)
	text = re.sub(
		r"\[\s+([^\[\]\{\}]+?)\s+\]",
		lambda match: f"[{' '.join(match.group(1).split())}]",
		text,
	)
	path.write_text(text, encoding="utf-8")
