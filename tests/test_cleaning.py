from pathlib import Path

import pytest

from tennis_career.data import _normalize_name, _clean_male, _parse_matches, _clean_female

FIXTURES = Path(__file__).parent / "fixtures"

def test_normalize_name():
    assert _normalize_name("serena williams") == "SerenaWilliams"
    assert _normalize_name("Serena Williams") == "SerenaWilliams"
    assert _normalize_name("SerenaWilliams") == "SerenaWilliams"

def test_normalize_extra_spaces():
    assert _normalize_name("  rafael   nadal ") == "RafaelNadal"

def test_parse_matches_female():
    rows = _parse_matches((FIXTURES / "FemalePlayerCareer.JS").read_text())
    assert len(rows) == 3
    assert rows[0][11] == "Anne Miller"


def test_parse_matches_male():
    rows = _parse_matches((FIXTURES / "MalePlayerCareer.JS").read_text())
    assert len(rows) == 3
    assert rows[0][11] == "Guillermo Platel"

def test_clean_male():
    rows = _parse_matches((FIXTURES / "MalePlayerCareer.JS").read_text())
    df = _clean_male(rows, "19860603")
    assert list(df.columns) == ["date", "tournament", "surface", "result", "round",
                                "opponent", "opp_age", "age", "age_diff"]
    assert df.loc[0, "result"] == "L"
    assert df.loc[0, "age"] == pytest.approx(15.27, abs=0.05)
    assert df.loc[0, "age_diff"] == pytest.approx(-6.99, abs=0.05)

def test_clean_female():
    rows = _parse_matches((FIXTURES / "FemalePlayerCareer.JS").read_text())
    df = _clean_female(rows, "19810926")
    assert df.loc[0, "result"] == "L"
    assert df.loc[0, "opp_age"] == pytest.approx(18.78, abs=0.05)
    assert df.loc[0, "age"] == pytest.approx(14.09, abs=0.05)
    assert df.loc[0, "age_diff"] == pytest.approx(-4.69, abs=0.05)