from tennis_career.data import _normalize_name

from pathlib import Path

from tennis_career.data import _normalize_name, _parse_matches

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