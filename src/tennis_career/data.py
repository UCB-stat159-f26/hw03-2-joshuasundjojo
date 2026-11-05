"""Fetch and clean tennis career data from tennisabstract.com."""

import json
import re

def _parse_matches(js_text):
    """Extract the list of match rows from a career JS file as Python lists."""
    match = re.search(r"\[\[.*?\]\]", js_text, re.DOTALL)
    return json.loads(match.group(0))

def _normalize_name(name):
    """Convert player name to the format used in tennisabstract"""
    words = name.split()
    return "".join(word[:1].upper() + word[1:] for word in words)