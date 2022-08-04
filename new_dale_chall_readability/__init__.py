__version__ = "0.2.0"


import re
from typing import Final
from .formulas import cloze_score
from .easy_words import EASY_WORDS

COMPENSATION_FACTOR = 1.265


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

    from devtools import debug

    debug(len(unfamiliar_words))

    return round(
        COMPENSATION_FACTOR
        * cloze_score(
            pct_unfamiliar_words=pct_unfamiliar_words,
            avg_sentence_length=avg_sentence_len,
        )
    )
