"""Fetch and clean tennis career data from tennisabstract.com."""

def _normalize_name(name):
    """Convert player name to the format used in tennisabstract"""
    words = name.split()
    return "".join(word[:1].upper() + word[1:] for word in words)