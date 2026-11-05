from tennis_career.data import _normalize_name

def test_normalize_name():
    assert _normalize_name("serena williams") == "SerenaWilliams"
    assert _normalize_name("Serena Williams") == "SerenaWilliams"
    assert _normalize_name("SerenaWilliams") == "SerenaWilliams"

def test_normalize_extra_spaces():
    assert _normalize_name("  rafael   nadal ") == "RafaelNadal"