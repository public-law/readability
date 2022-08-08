from pytest import approx  # type: ignore
from new_dale_chall_readability import cloze_score, reading_level


"""
Test the high-level API for end-users. Luckily, _Readability Revisited_
provides great test cases in the form of sample passages that have been
scored by the authors. These tests use the samples directly to make
sure the library gives the expected output.
"""


# Reading level 3 (Chall & Dale, page 146):
#   Number of Words in Sample: 100
#   Number of Whole Sentences: 8
#   Number of Unfamiliar words: 3
#   Cloze score: 53
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

class TestSampleTextLevel_3:
    def test_cloze_score(self):
        assert cloze_score(HIGHLIGHTS_FOR_CHILDREN) == approx(53.0, abs=0.01)

    def test_reading_level(self):
        assert reading_level(HIGHLIGHTS_FOR_CHILDREN) == "3"


# Reading level 13-15 (Chall & Dale, page 149):
#   Number of Words in Sample: 100
#   Number of Whole Sentences: 5
#   Number of Unfamiliar words: 35
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

class TestSampleTextLevel_13_15:
    def test_cloze_score(self):
        assert cloze_score(PSYCHOLOGY_TODAY) == approx(17.0, abs=0.01)

    def test_reading_level(self):
        assert reading_level(PSYCHOLOGY_TODAY) == "13-15"


# Reading Level 16+ (Chall & Dale, p. 150).
#   Number of Words in Sample: 100
#   Number of Whole Sentences: 2
#   Number of Unfamiliar words: 37
#   Cloze Score: -6
#   Reading Level: "16+"
HARVARD_ED_REV = """
Further support for the view that educational expansion would reduce
inequalities was derived from the dualistic nature of developing
societies. The economic structures of developing societies were said to 
consist of two sectors: a traditional sector that uses little capital,
is relatively unproductive, does not require an educated labor force,
and places a great emphasis on subsistence farming, small workshops and
small commercial enterprises: and a modern sector that uses advanced
technology and capital, is far more productive, and requires a labor
force with at least some schooling. Expanding the educational system 
would qualify more workers for jobs where demands
"""

# "schooling" and "workshop[s]" are easy words according to the text but
# are not in easy_words.py.
#
# Checking with the book, it's the same as the python file:
#
# "schooling" is not in the easy words list on p. 26. "school" is, though.
# "workshop" is not in the list (p. 29). "work" is. (?)
#
# On p. 16 is the note:
#
# "Consider as known words on the list with endings indicated in
#  parentheses and words with the following endings, even though
#  they are not noted in parentheses:
#    -'s, -s, -es, -ies; -d, -ed, -ied, -ing; -r, -er, -est, -ier, -est
#
#  (For further instructions, see pages 13–15.)"
#
class TestSampleTextLevel_16_plus:
    def test_cloze_score(self):
        assert cloze_score(HARVARD_ED_REV) == approx(-6.0, abs=0.01)

    def test_reading_level(self):
        assert reading_level(HARVARD_ED_REV) == "16+"


# References
#
# Chall, J., & Dale, E. (1995). _Readability revisited: The new Dale-Chall readability formula_.
# Brookline Books.
