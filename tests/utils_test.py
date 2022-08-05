from new_dale_chall_readability.utils import pct_unfamiliar_words


class DescribePctUnfamiliarWords:
    def it_handles_all_familiar(self):
        input = "Dog cat play house."

        assert pct_unfamiliar_words(input) == 0.0

    def it_handles_repeated_uses(self):
        input = "Dog respondent dog respondent dog respondent."

        assert pct_unfamiliar_words(input) == 0.5

    def it_handles_mixed_uses(self):
        input = "Dog raconteur dog respondent dog respondent."

        assert pct_unfamiliar_words(input) == 0.5

    def it_handles_all_unfamiliar(self):
        input = "Deponent deponent deponent."

        assert pct_unfamiliar_words(input) == 1.0
