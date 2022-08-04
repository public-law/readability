from pytest import approx

from new_dale_chall_readability.formulas import (
    cloze_score,
    reading_level_from_cloze,
    reading_level,
)
from new_dale_chall_readability import cloze_score_from_text, reading_level_from_text


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


# Reading Level 3 sample text. (Page 146)
# Sentences: 8
# Unfamiliar words: 3
# Clozed score: 53
# Reading level: "3"
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

# Reading level 13-15 sample text. (Page 149)
# Sentences: 5
# Unfamiliar words: 35
# Cloze Score: 17
# Reading Level: "13-15"
PSYCHOLOGY_TODAY = """
Until the 1940's, there were no specific psychiatric drugs. Bromides,
barbituates, and opiates were known to sedate disturbed patients but
did not reverse the symptoms of severe mental illnesses such as the
schizophrenias or manic-depressive psychoses. They did ameliorate anxiety,
but only at the cost of fogging the minds of the recipients, who had to
decide between being unhappy and being intoxicated. In the 1950's, the
first specific drug appeared: chlorpromazine (trade name Thorazine). It
was synthesized when an antihiatamine chemical relative was found to
sedate surgical patients. However, clinical observations showed that this
drug did much more than simply
"""


class TestClozeScoreFromText:
    def test_reading_level_3(self):
        assert cloze_score_from_text(HIGHLIGHTS_FOR_CHILDREN) == approx(53, abs=0.1)

    def test_reading_level_13_15(self):
        assert cloze_score_from_text(PSYCHOLOGY_TODAY) == approx(17, abs=0.1)


class TestReadingLevelFromText:
    def test_reading_level_3(self):
        assert reading_level_from_text(HIGHLIGHTS_FOR_CHILDREN) == "3"

    def test_reading_level_13_15(self):
        assert reading_level_from_text(PSYCHOLOGY_TODAY) == "13-15"
