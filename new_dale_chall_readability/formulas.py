import math
from typing import Any, Literal, TypeAlias


def compute_cloze_score(
    pct_unfamiliar_words: float, avg_sentence_length: float
) -> float:
    """
    Compute the Cloze score (Chall & Dale, 1995, p.66).
    Table 2-1 shows cloze scores rounded to two decimal places. This
    function follows suit.
    """
    raw_result = 64 - (95 * pct_unfamiliar_words) - (0.69 * avg_sentence_length)

    return round(raw_result, 2)


"""
Reading levels are enums. They're strings, not integers. See, e.g.:
Table 5-8, p. 74.
"""
ReadingLevel: TypeAlias = Literal[
    "1", "2", "3", "4", "5-6", "7-8", "9-10", "11-12", "13-15", "16+"
]


class RangeDict(dict[range, ReadingLevel]):
    """
    A dictionary that maps a range of cloze scores to reading level.
    """

    def __getitem__(self, item: Any) -> ReadingLevel:
        """
        Iterate over the intervals. If the argument is in that interval
        return its associated value. If not in any interval, raise KeyError.
        """
        int_item = math.ceil(item)

        for key in self.keys():
            if int_item in key:
                return super().__getitem__(key)

        raise KeyError(item)


"""
From Table 5-8, p. 74.
"""
ARBITRARY_MAX = 64
ARBITRARY_MIN = 10
EQUIV_CLOZE_AND_READING_LEVELS = RangeDict(
    {
        range(58, ARBITRARY_MAX + 1): "1",
        range(54, 58): "2",
        range(50, 54): "3",
        range(45, 50): "4",
        range(40, 45): "5-6",
        range(34, 40): "7-8",
        range(28, 34): "9-10",
        range(22, 28): "11-12",
        range(16, 22): "13-15",
        range(ARBITRARY_MIN, 16): "16+",
    }
)


def reading_level_from_cloze(cloze_score: float) -> ReadingLevel:
    """
    Translate the given cloze score to a reading level. See: Table 5-8, p. 74.
    """
    bounded_score = max(ARBITRARY_MIN, min(ARBITRARY_MAX, cloze_score))

    return EQUIV_CLOZE_AND_READING_LEVELS[bounded_score]


def compute_reading_level(
    pct_unfamiliar_words: float, avg_sentence_length: float
) -> ReadingLevel:
    """
    Compute the reading level.
    """
    return reading_level_from_cloze(
        compute_cloze_score(pct_unfamiliar_words, avg_sentence_length)
    )
