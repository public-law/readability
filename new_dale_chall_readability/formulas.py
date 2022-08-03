from typing import Literal, TypeAlias


ReadingLevel: TypeAlias = Literal[
    "1", "2", "3", "4", "5-6", "7-8", "9-10", "11-12", "13-15", "16+"
]

"""
See Table 5-8, p. 74.
"""
EQUIV_CLOZE_AND_READING_LEVELS: dict[tuple[int | None, int | None], ReadingLevel] = {
    (57, None): "1",
    (53, 57): "2",
    (49, 53): "3",
    (44, 49): "4",
    (39, 44): "5-6",
    (33, 39): "7-8",
    (27, 33): "9-10",
    (21, 27): "11-12",
    (15, 21): "13-15",
    (None, 15): "16+",
}


def cloze_score(pct_unfamiliar_words: float, avg_sentence_length: float) -> float:
    """
    Compute the Cloze score (Chall & Dale, 1995, p.66).
    Table 2-1 shows cloze scores rounded to two decimal places. This
    function follows suit.
    """
    raw_result = 64 - (95 * pct_unfamiliar_words) - (0.69 * avg_sentence_length)

    return round(raw_result, 2)


def reading_level_from_cloze(cloze_score: float) -> ReadingLevel:
    """
    Compute the reading level from the Cloze score.
    """
    for keys in EQUIV_CLOZE_AND_READING_LEVELS:
        if cloze_score > keys[0] and cloze_score <= keys[1]:
            return EQUIV_CLOZE_AND_READING_LEVELS[keys]

    raise ValueError(f"(Unreachable) Cloze score {cloze_score} is out of range.")
