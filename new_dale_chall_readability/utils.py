import re
import warnings

from bs4 import BeautifulSoup
from .easy_words import EASY_WORDS as _EASY_WORDS

# Ignore MarkupResemblesLocatorWarning and other user warnings
# because this is library code.
warnings.filterwarnings("ignore", category=UserWarning, module="bs4")


def pct_unfamiliar_words(text: str) -> float:
    words = _words(text)
    no_possesives = (w.replace("'s", "").replace("s'", "") for w in words)
    unfamiliar_words = [w for w in no_possesives if _is_unfamiliar(w)]

    return len(unfamiliar_words) / len(words)


def avg_sentence_length(text: str) -> float:
    cleaned_up_text = text.replace("\n", " ").strip()
    sentences = re.findall(r"\b[^.!?]+[.!?]*", cleaned_up_text, re.UNICODE)
    #prevents division of zero error
    if not sentences:
        return 0.0
    words = _words(text)

    return len(words) / len(sentences)


def _words(in_text: str) -> tuple[str, ...]:
    plain_text = BeautifulSoup(in_text, "html.parser").text

    return tuple(w.lower().strip('.(),"') for w in plain_text.split())


def _is_unfamiliar(word: str) -> bool:

    """
    Determine if a word is considered unfamiliar according to the Dale-Chall formula.
    
    A word is considered familiar if it is either:
    1. A number (e.g., "2020", "15")
    2. Present in the Dale-Chall list of familiar words
    
    The Dale-Chall list contains approximately 3,000 words that were empirically 
    determined to be familiar to most fourth-grade students.
    
    Args:
        word: A single word, stripped of punctuation and converted to lowercase
        
    Returns:
        bool: True if the word is unfamiliar, False if familiar
        
    Examples:
        >>> _is_unfamiliar("dog")  # In easy word list
        False
        >>> _is_unfamiliar("2020")  # A number
        False
        >>> _is_unfamiliar("raconteur")  # Not in easy word list
        True
    """
    if word.isdigit():
        return False
        
    return word not in _EASY_WORDS
