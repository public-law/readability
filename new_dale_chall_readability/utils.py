import re
from .easy_words import EASY_WORDS as _EASY_WORDS


def pct_unfamiliar_words(text: str) -> float:
    words = [w.lower().strip('.(),"') for w in text.split()]
    no_possesives = (w.replace("'s", "").replace("s'", "") for w in words)
    unfamiliar_words = [w for w in no_possesives if w not in _EASY_WORDS]

    return len(unfamiliar_words) / len(words)


def avg_sentence_length(text: str) -> float:
    cleaned_up_text = text.replace("\n", " ").strip()
    sentences = re.findall(r"\b[^.!?]+[.!?]*", cleaned_up_text, re.UNICODE)
    words = [w.lower().strip('.(),"') for w in text.split()]

    return len(words) / len(sentences)
