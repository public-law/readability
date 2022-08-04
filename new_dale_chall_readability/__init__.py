__version__ = "0.2.0"

import re
from .formulas import ReadingLevel, cloze_score, reading_level_from_cloze
from .easy_words import EASY_WORDS

# Compensate for the inaccurate easy word search.
COMPENSATION_FACTOR_1 = 1.35
COMPENSATION_FACTOR_2 = 1.23


def cloze_score_from_text(text: str) -> float:
    """
    Calculate the cloze score from the given text.
    """
    cleaned_up_text = text.replace("\n", " ").strip()
    sentences = re.findall(r"\b[^.!?]+[.!?]*", cleaned_up_text, re.UNICODE)
    words = [w.lower().strip('.(),"') for w in text.split()]

    unfamiliar_words = [w for w in words if w not in EASY_WORDS]

    pct_unfamiliar_words = len(unfamiliar_words) / len(words)
    avg_sentence_len = len(words) / len(sentences)

    raw_score = cloze_score(
        pct_unfamiliar_words=pct_unfamiliar_words,
        avg_sentence_length=avg_sentence_len,
    )

    compensation_factor = (
        COMPENSATION_FACTOR_1 if raw_score < 40 else COMPENSATION_FACTOR_2
    )

    return compensation_factor * raw_score


def reading_level_from_text(text: str) -> ReadingLevel:
    """
    Calculate the reading level of the given text.
    """
    return reading_level_from_cloze(cloze_score_from_text(text))
