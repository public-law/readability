from new_dale_chall_readability.utils import pct_unfamiliar_words


def it_handles_repeated_uses():
    input = "Dog respondent dog respondent dog respondent."

    assert pct_unfamiliar_words(input) == 0.5


def it_handles_mixed_uses():
    input = "Dog raconteur dog respondent dog respondent."

    assert pct_unfamiliar_words(input) == 0.5


def test_all_familiar():
    input = "Dog cat play house."

    assert pct_unfamiliar_words(input) == 0.0
