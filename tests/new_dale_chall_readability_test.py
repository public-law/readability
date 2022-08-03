from new_dale_chall_readability.formulas import compute_cloze


def test_with_round_numbers():
    """
    Test case extracted from Chall and Dale (1985, page 31, Table 2.1).
    """
    assert compute_cloze(pct_unfamiliar_words=0.2, avg_sentence_length=10.0) == 38.1


def test_a_higher_result():
    """
    Test case extracted from Chall and Dale (1985, page 33, Table 2.1).
    """
    assert (
        compute_cloze(pct_unfamiliar_words=0.11, avg_sentence_length=100 / 27) == 50.99
    )
