import re
import warnings

from bs4 import BeautifulSoup
from .easy_words import EASY_WORDS as _EASY_WORDS

# Ignore MarkupResemblesLocatorWarning and other user warnings
# because this is library code.
warnings.filterwarnings("ignore", category=UserWarning, module="bs4")


def pct_unfamiliar_words(text: str) -> float:
    """
    Calculates the percentage of unfamiliar words in a string.

    step1: calls all words in a tuple from _words.
    step2: removes the possesives from any words in said tuple.
    step3: counts the number of unfamiliar words from cleaned tuple using _is_unfamiliar.
    step3: returns the percentage by dividing the length of unfamiliar words by words.
    """
    words = _words(text)
    if not words:
        return 0.0
    no_possesives = (w.replace("'s", "").replace("s'", "") for w in words)
    unfamiliar_words = [w for w in no_possesives if _is_unfamiliar(w)]

    return len(unfamiliar_words) / len(words)


def avg_sentence_length(text: str) -> float:
    """
    Calculates average number of words per sentence in text.

    step1: remove newlines and trailing white space from text.
    step2: seperates text into sentances based on non-punctuation characters
    followed by an optional punctuation
    step3: calls _words to return all words in a tuple
    step4: returns the average length by dividing the length of words to the length
    of sentences.
    """
    cleaned_up_text = text.replace("\n", " ").strip()
    sentences = re.findall(r"\b[^.!?]+[.!?]*", cleaned_up_text, re.UNICODE)
    #prevents division of zero error
    if not sentences:
        return 0.0
    words = _words(text)

    return len(words) / len(sentences)


def _words(in_text: str) -> tuple[str, ...]:
    """
    Takes the plain text that is entered and returns a tuple of words.

    Args:
        in_text: an string of words that includes HTML tags, punctuation marks, and capital words.
        otherwise known as plain_text.
    Returns:
        tuple: a tuple of individual words that are stripped of HTML tags, punctuation marks, 
        and turns Capital letters into lower case.

    Example:
        text = <p>The excited child ran to the park, yelling, 'Look, a big red ball!'
        as she chased after it, laughing with glee.</p>
        words = _words(text) # ("the", "excited", "child", etc...)
    """
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
