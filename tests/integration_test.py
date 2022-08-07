from pytest import approx  # type: ignore
from new_dale_chall_readability import cloze_score, reading_level


"""
Test the High-level API for end-users of the library.
"""


# Reading level 3 sample text (page 146):
#   Sentences: 8
#   Unfamiliar words: 3
#   Clozed score: 53
#   Reading level: "3"
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

class TestSampleTextLevel3:
    def test_cloze_score(self):
        assert cloze_score(HIGHLIGHTS_FOR_CHILDREN) == approx(53.0, abs=0.01)

    def test_reading_level(self):
        assert reading_level(HIGHLIGHTS_FOR_CHILDREN) == "3"


# Reading level 13-15 sample text (page 149):
#   Sentences: 5
#   Unfamiliar words: 35
#   Cloze Score: 17
#   Reading Level: "13-15"
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

class TestSampleTextLevel13_15:
    def test_cloze_score(self):
        assert cloze_score(PSYCHOLOGY_TODAY) == approx(17.0, abs=0.01)

    def test_reading_level(self):
        assert reading_level(PSYCHOLOGY_TODAY) == "13-15"
