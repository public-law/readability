from pytest import approx

from new_dale_chall_readability.formulas import (
    cloze_score,
    reading_level_from_cloze,
    reading_level,
)
from new_dale_chall_readability import cloze_score_from_text


class TestClozeScore:
    def test_with_round_numbers(self):
        """
        Test case extracted from Chall and Dale (1995, page 31, Table 2.1).
        """
        assert cloze_score(pct_unfamiliar_words=0.2, avg_sentence_length=10.0) == 38.1

    def test_a_higher_result(self):
        """
        Test case extracted from Chall and Dale (1995, page 33, Table 2.1).
        """
        assert (
            cloze_score(pct_unfamiliar_words=0.11, avg_sentence_length=100 / 27)
            == 50.99
        )


class TestReadingLevelFromCloze:
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


class TestReadingLevel:
    def test_with_round_numbers(self):
        assert (
            reading_level(pct_unfamiliar_words=0.2, avg_sentence_length=10.0) == "7-8"
        )

    def test_a_higher_result(self):
        assert (
            reading_level(pct_unfamiliar_words=0.11, avg_sentence_length=100 / 27)
            == "3"
        )


# Reading Level 3 asmple text. (Page 146)
HIGHLIGHTS_FOR_CHILDREN = """
Once upon a time a very small witch was walking in the woods. The cold
wind was blowing the dry leaves all around her. The little witch was
frantically searching for a house for the winter. She could not find one.
Suddenly a piece of orange paper, blown by the wind, landed at her feet.
She picked it up.

The little witch looked closely at the paper and then she said,
"I shall make myself a little house from this piece of orange paper."

She folded the paper in half. Then she took her scissors (she always
carried a pair
"""


class TestClozeScoreFromText:
    def test_reading_level_3(self):
        assert cloze_score_from_text(HIGHLIGHTS_FOR_CHILDREN) == approx(53, abs=1)

    # def test_reading_level_13_15(self):
    #     assert cloze_score_from_text(HIGHLIGHTS_FOR_CHILDREN) == approx(53, abs=1)
