"""Fetch and clean tennis career data from tennisabstract.com."""

import json
import re
import pandas as pd
import requests

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

def _add_ages(df, dob):
    """Add the player's age and the age difference."""
    born = pd.to_datetime(str(dob), format="%Y%m%d")
    df["age"] = _years_between(born, df["date"])
    df["age_diff"] = df["age"] - df["opp_age"]
    return df    

def _clean_male(rows, dob):
    """Clean a male player's rows; the opponent's age is given directly."""
    df = _base_frame(rows)
    df["opp_age"] = pd.to_numeric(df.pop("opp_info"), errors="coerce")
    return _add_ages(df, dob)

def _clean_female(rows, dob):
    """Clean a female player's rows; opponent age is derived from their birthday."""
    df = _base_frame(rows)
    opp_born = pd.to_datetime(df.pop("opp_info"), format="%Y%m%d", errors="coerce")
    df["opp_age"] = _years_between(opp_born, df["date"])
    return _add_ages(df, dob)

def _is_female(rows):
    """Female rows list the opponent's birthday (8 digits); male rows give an age."""
    return any(re.fullmatch(r"\d{8}", str(row[16])) for row in rows)


def _find_dob(html):
    """Pull the player's birthday (yyyymmdd) out of a player page's text."""
    match = re.search(r"dob\s*=\s*(\d{8})", html)
    if match is None:
        raise ValueError("Could not find this player's date of birth.")
    return match.group(1)

BASE_URL = "https://www.tennisabstract.com"

def _fetch_career(name):
    """Download a player's career JS file; raise a clear error if the player is unknown."""
    response = requests.get(f"{BASE_URL}/jsmatches/{name}Career.js", timeout=30)
    if response.status_code == 404:
        raise ValueError(f"No player found for '{name}'. Check the full name's spelling.")
    response.raise_for_status()
    return response.text