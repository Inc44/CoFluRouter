from __future__ import annotations
from typing import List, Tuple
import argparse
import ast


class Config:
	def __init__(self, args: argparse.Namespace):
		self.accessibility: List[Tuple[int, int, int]] = (
			ast.literal_eval(f"[{args.accessibility}]") if args.accessibility else []
		)
		self.fetch: bool = args.fetch
		self.update: bool = args.update
