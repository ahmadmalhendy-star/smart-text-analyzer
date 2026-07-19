
import re

def replace_word(text: str, old_word: str, new_word: str) -> str:
    """
    Replaces only full, standalone occurrences of old_word with new_word.
    Protects against partial matching inside larger words.
    """
    if not text or not old_word:
        return text

    # \b acts as an anchor matching the boundary between a word character and a non-word character
    # re.escape ensures special characters in the word don't break the regex compiler
    pattern = re.compile(r'\b' + re.escape(old_word) + r'\b', re.IGNORECASE)
    
    return pattern.sub(new_word, text)