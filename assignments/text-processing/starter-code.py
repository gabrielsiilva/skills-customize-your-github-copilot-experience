"""Starter code for the Text Processing assignment.

Contains stubs for:
- clean_text(text: str) -> str
- word_frequencies(text: str) -> dict
- top_n_words(freqs: dict, n: int) -> list[tuple[str,int]]

Run as a script to see a small demo.
"""
from collections import Counter
import re
from typing import Dict, List, Tuple


def clean_text(text: str) -> str:
    """Lowercase the text, remove punctuation, and collapse whitespace to single spaces."""
    if not text:
        return ""
    # Keep alphanumeric characters and whitespace
    text = text.lower()
    # Replace any non-alphanumeric (except whitespace) with space
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    # Collapse multiple whitespace to single space and strip
    text = re.sub(r"\s+", " ", text).strip()
    return text


def word_frequencies(text: str) -> Dict[str, int]:
    """Return a mapping of word -> count for the provided text.

    The function will clean the text first using `clean_text`.
    """
    cleaned = clean_text(text)
    if not cleaned:
        return {}
    words = cleaned.split(" ")
    # Use Counter for convenience
    return dict(Counter(w for w in words if w))


def top_n_words(freqs: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    """Return the top `n` words as a list of (word, count), ordered by count desc then word."""
    if not freqs:
        return []
    # Sort by count descending, then word ascending
    items = sorted(freqs.items(), key=lambda kv: (-kv[1], kv[0]))
    return items[:n]


def _demo():
    sample = """
    Hello, world! Hello world. This is a test: test, testing; TEST.
    New-lines, tabs	and multiple   spaces should be handled.
    """
    print("Original:\n", sample)
    cleaned = clean_text(sample)
    print("\nCleaned:\n", cleaned)
    freqs = word_frequencies(sample)
    print("\nFrequencies:\n", freqs)
    print("\nTop 5:\n", top_n_words(freqs, 5))


if __name__ == "__main__":
    _demo()
