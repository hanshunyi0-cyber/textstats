from textstats import word_count, char_frequencies, longest_word


def test_word_count_empty():
    assert word_count("") == 0


def test_word_count_single_word():
    assert word_count("hello") == 1


def test_word_count_multiple_words():
    assert word_count("the quick brown fox") == 4

def test_char_frequencies_ignores_case():
    assert char_frequencies("AaBb") == {
        "a": 2,
        "b": 2,
    }


def test_char_frequencies_ignores_whitespace():
    assert char_frequencies("a b\tc\n") == {
        "a": 1,
        "b": 1,
        "c": 1,
    }


def test_char_frequencies_counts_punctuation_and_digits():
    assert char_frequencies("A1!") == {
        "a": 1,
        "1": 1,
        "!": 1,
    }
