def word_count(text: str) -> int:
    """Number of whitespace-separated tokens in `text`."""
    return len(text.split())

def char_frequencies(text: str) -> dict[str, int]:
    """Count of each character, ignoring whitespace and case."""
    
    frequencies = {}

    for char in text.lower():
        if not char.isspace():
            frequencies[char] = frequencies.get(char, 0) + 1

    return frequencies

def longest_word(text: str) -> str:
    """The longest token. Raises ValueError on empty input."""
    if not text or text.isspace():
        raise ValueError("empty input")
    tokens = text.split()
    return max(tokens, key=len)