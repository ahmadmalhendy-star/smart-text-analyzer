# core/autocomplete.py
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


def get_autocomplete_suggestions(document: TextDocument, prefix: str, limit: int = 5) -> list:
    """
    Suggest words that start with the prefix, optimized using the document's pre-compiled words.
    """
    prefix = clean_prefix(prefix)

    if prefix == "" or document.is_empty():
        return []

    # Count frequencies only for words matching the prefix (O(N) search over single flat list)
    frequency = {}
    for word in document.words:
        if word.startswith(prefix):
            frequency[word] = frequency.get(word, 0) + 1

    # Convert to list of pairs for sorting
    suggestions = [(word, count) for word, count in frequency.items()]

    # Sort: Frequency descending (-item[1]), then alphabetical order (item[0])
    suggestions.sort(key=lambda item: (-item[1], item[0]))

    # Extract only the top words up to the requested limit
    return [word for word, count in suggestions[:limit]]


def print_autocomplete_suggestions(suggestions: list, prefix: str) -> None:
    """
    Print autocomplete suggestions.
    """
    cleaned_prefix = clean_prefix(prefix)
    if len(suggestions) == 0:
        print(f"\nNo suggestions found matching prefix: '{cleaned_prefix}'")
        return

    print(f"\nSuggestions for: '{cleaned_prefix}'")
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
            print("Autocomplete session ended.")
            break

        suggestions = get_autocomplete_suggestions(document, prefix)
        print_autocomplete_suggestions(suggestions, prefix)