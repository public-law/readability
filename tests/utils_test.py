from new_dale_chall_readability.utils import pct_unfamiliar_words


class TestPctUnfamiliarWords:
    def test_all_familiar(self):
        input = "Dog cat play house."

        assert pct_unfamiliar_words(input) == 0.0

    def test_repeated_uses(self):
        input = "Dog respondent dog respondent dog respondent."

        assert pct_unfamiliar_words(input) == 0.5

    def test_mixed_uses(self):
        input = "Dog raconteur dog respondent dog respondent."

        assert pct_unfamiliar_words(input) == 0.5

    def test_all_unfamiliar(self):
        input = "Deponent deponent deponent."

        assert pct_unfamiliar_words(input) == 1.0

    def test_possessives(self):
        input = "Dog's dog's dog's."

        assert pct_unfamiliar_words(input) == 0.0

    def test_plural_possessives(self):
        input = "Dogs' dog's dogs'."

        assert pct_unfamiliar_words(input) == 0.0

    def test_embedded_html(self):
        input = "Dog <em>dog</em> dog."

        assert pct_unfamiliar_words(input) == 0.0

    def test_embedded_year(self):
        input = "A dog born in 2020."

        assert pct_unfamiliar_words(input) == 0.0

    def test_embedded_ages(self):
        input = "A boy or girl aged 14, 15 or 16."

        assert pct_unfamiliar_words(input) == 0.0
