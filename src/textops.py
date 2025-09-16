from typing import List
from collections import Counter

def unique_words_preserve_order(words: List[str]) -> List[str]:
    """Return first occurrences only (case-sensitive)."""
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result


def top_k_frequent_first_tie(words: List[str], k: int) -> List[str]:
    """Return up to k words ordered by frequency (high to low). Ties: first occurrence wins."""
    if k <= 0:
        raise ValueError("k must be positive")

    # Count frequencies
    freq = Counter(words)
    # Keep the order of first appearance
    first_seen = {word: i for i, word in enumerate(words)}
    
    # Sort by frequency descending, then by first appearance
    sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], first_seen[w]))
    
    return sorted_words[:k]


def redact_words(words: List[str], banned: List[str]) -> List[str]:
    """Return a new list where every word in `banned` is replaced by "***"."""
    banned_set = set(banned)
    return [ "***" if word in banned_set else word for word in words ]
