import pytest
from src.textops import unique_words_preserve_order, top_k_frequent_first_tie, redact_words


def test_unique_words_preserve_order():
    assert unique_words_preserve_order(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]
    assert unique_words_preserve_order([]) == []


def test_top_k_frequent_first_tie():
    words = ["x", "y", "x", "z", "y", "y", "x"]
    # counts: x=3, y=3, z=1; first appearance: x(0) beats y(1)
    assert top_k_frequent_first_tie(words, 2) == ["x", "y"]
    with pytest.raises(ValueError):
        top_k_frequent_first_tie(words, 0)


def test_redact_words():
    words = ["alice", "bob", "alice", "carol"]
    assert redact_words(words, ["alice"]) == ["***", "bob", "***", "carol"]
    assert redact_words(words, []) == words