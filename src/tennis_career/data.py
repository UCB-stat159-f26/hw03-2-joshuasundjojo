"""Fetch and clean tennis career data from tennisabstract.com."""

import json
import re
import pandas as pd

def _normalize_name(name):
    """Convert player name to the format used in tennisabstract"""
    words = name.split()
    return "".join(word[:1].upper() + word[1:] for word in words)

def _parse_matches(js_text):
    """Extract the list of match rows from a career JS file as Python lists."""
    match = re.search(r"\[\[.*?\]\]", js_text, re.DOTALL)
    return json.loads(match.group(0))

KEEP = {0: "date", 1: "tournament", 2: "surface", 4: "result",
        8: "round", 11: "opponent", 16: "opp_info"}

def _base_frame(rows):
    """Keep the shared columns of the raw rows and parse the match dates."""
    df = pd.DataFrame(rows).iloc[:, list(KEEP)]
    df.columns = list(KEEP.values())
    df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")
    return df

    def _years_between(start, end):
    """Time in years between two dates."""
    return (end - start).dt.days / 365.25

    