from Models.text_document import TextDocument


def clean_prefix(prefix: str) -> str:
    """
    Clean the prefix entered by the user without using re.
    """
    prefix = prefix.lower().strip()

    cleaned = ""

    for char in prefix:
        if char.isalnum():
            cleaned += char

    return cleaned


def get_all_words_from_sentences(document: TextDocument) -> list:
    """
    Get all words from document.sentences.
    This is better than document.wrods because sentences are already clean.
    """
    words = []

    for sentence in document.sentences:
        for word in sentence:
            words.append(word)

    return words


def build_word_frequency(words: list) -> dict:
    """
    Count how many times each word appears.
    """
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def get_autocomplete_suggestions(document: TextDocument, prefix: str, limit: int = 5) -> list:
    """
    Suggest words that start with the prefix.
    """
    prefix = clean_prefix(prefix)

    if prefix == "":
        return []

    if document.is_empty():
        return []

    words = get_all_words_from_sentences(document)
    frequency = build_word_frequency(words)

    suggestions = []

    for word in frequency:
        if word.startswith(prefix) and word != prefix:
            suggestions.append((word, frequency[word]))

    suggestions.sort(key=lambda item: (-item[1], item[0]))

    final_suggestions = []

    for word, count in suggestions:
        final_suggestions.append(word)

        if len(final_suggestions) == limit:
            break

    return final_suggestions


def print_autocomplete_suggestions(suggestions: list, prefix: str) -> None:
    """
    Print autocomplete suggestions.
    """
    if len(suggestions) == 0:
        print(f"\nNo suggestions found for: {prefix}")
        return

    print(f"\nSuggestions for: {prefix}")
    print("-" * 30)

    for index, word in enumerate(suggestions, start=1):
        print(f"{index}. {word}")


def autocomplete_prompt(document: TextDocument) -> None:
    """
    Ask the user to enter a prefix and show suggestions.
    """
    while True:
        prefix = input("\nEnter the beginning of a word, or type 'q' to quit: ").strip()

        if prefix.lower() == "q":
            print("Autocomplete ended.")
            break

        suggestions = get_autocomplete_suggestions(document, prefix)
        print_autocomplete_suggestions(suggestions, prefix)