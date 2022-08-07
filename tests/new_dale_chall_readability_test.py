from pytest import approx  # type: ignore   (Pyright doesn't like approx().)

from new_dale_chall_readability.formulas import (
    compute_cloze_score,
    reading_level_from_cloze,
    compute_reading_level,
)

"""
Unit tests for the library.
"""

class TestClozeScore:
    def test_with_round_numbers(self):
        """
        Test case extracted from Chall and Dale (1995, page 31, Table 2.1).
        """
        assert (
            compute_cloze_score(pct_unfamiliar_words=0.2, avg_sentence_length=10.0)
            == 38.1
        )

    def test_a_higher_result(self):
        """
        Test case extracted from Chall and Dale (1995, page 33, Table 2.1).
        """
        assert (
            compute_cloze_score(pct_unfamiliar_words=0.11, avg_sentence_length=100 / 27)
            == 50.99
        )


class TestReadingLevelFromCloze:
    """
    Test the library's ability to convert a floating point
    cloze score into one of the 10 string reading levels.
    """
    def test_a_lowest_bound(self):
        assert reading_level_from_cloze(39.01) == "5-6"

    def test_the_upper_bound(self):
        assert reading_level_from_cloze(44.0) == "5-6"

    def test_a_very_difficult_score(self):
        assert reading_level_from_cloze(11.2) == "16+"

    def test_a_very_easy_score(self):
        assert reading_level_from_cloze(64.0) == "1"

    def test_lower_boundary(self):
        assert reading_level_from_cloze(15) == "16+"


class TestComputeReadingLevel:
    """
    This function didn't end up getting used in the higher-level code.
    TODO: Possibly delete this function and the tests.
    """
    def test_with_round_numbers(self):
        assert (
            compute_reading_level(pct_unfamiliar_words=0.2, avg_sentence_length=10.0)
            == "7-8"
        )

    def test_a_higher_result(self):
        assert (
            compute_reading_level(
                pct_unfamiliar_words=0.11, avg_sentence_length=100 / 27
            )
            == "3"
        )
