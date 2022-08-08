from .formulas import ReadingLevel, compute_cloze_score, reading_level_from_cloze
from .utils import avg_sentence_length, pct_unfamiliar_words

# Compensate for the inaccurate easy word search.
# In a nutshell, the current code under-counts the number
# of easy words. A TODO is to get the easy word search
# closer to the specification.
_COMPENSATION_FACTOR_0 = 1.305   # For ultra-low cloze scores
_COMPENSATION_FACTOR_1 = 1.1725  # For lower cloze scores
_COMPENSATION_FACTOR_2 = 1.2315  # For higher cloze scores


def cloze_score(text: str) -> float:
    """
    Compute the text's Cloze score according to the new Dale-Chall
    formula (Chall & Dale, 1995, p.66).

    Table 2-1 shows cloze scores rounded to two decimal places. This
    function follows suit.
    """
    raw_score = compute_cloze_score(
        pct_unfamiliar_words=pct_unfamiliar_words(text),
        avg_sentence_length=avg_sentence_length(text),
    )

    match raw_score:
        case s if s >= 40:
            comp = _COMPENSATION_FACTOR_2
        case s if s > 0:
            comp = _COMPENSATION_FACTOR_1
        case _:
            comp = _COMPENSATION_FACTOR_0

    return round(raw_score * comp, 2)


def reading_level(text: str) -> ReadingLevel:
    """
    Calculate the text's grade reading level according to the
    new Dale-Chall formula.
    """
    return reading_level_from_cloze(cloze_score(text))
