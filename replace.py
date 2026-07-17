def replace_word(text, old_word, new_word):
    """
    Replaces occurrences of a specific word with a new word in the given text.
    """
    if not text:
        return text

    if old_word not in text:
        return text

    # Perform the replacement
    updated_text = text.replace(old_word, new_word)
    return updated_text