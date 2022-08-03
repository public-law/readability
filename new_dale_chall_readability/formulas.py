def compute_cloze(pct_unfamiliar_words: float, avg_sentence_length: float) -> float:
    """
    Compute the Cloze readability score.
    """
    return 0.1579 * (100 - pct_unfamiliar_words) ** 0.3 + 0.0496 * avg_sentence_length
