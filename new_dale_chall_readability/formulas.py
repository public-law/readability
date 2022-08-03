def cloze(pct_unfamiliar_words: float, avg_sentence_length: float) -> float:
    """
    Compute the Cloze score (Chall & Dale, 1995, p.66).
    Table 2-1 shows cloze scores rounded to two decimal places. This
    function follows suit.
    """
    raw_result = 64 - (95 * pct_unfamiliar_words) - (0.69 * avg_sentence_length)

    return round(raw_result, 2)
