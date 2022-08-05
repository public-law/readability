from .easy_words import EASY_WORDS as _EASY_WORDS


def pct_unfamiliar_words(text: str) -> float:
    words = [w.lower().strip('.(),"') for w in text.split()]
    unfamiliar_words = [w for w in words if w not in _EASY_WORDS]

    return len(unfamiliar_words) / len(words)
