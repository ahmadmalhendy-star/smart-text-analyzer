# core/search.py
from Models.text_document import TextDocument

def clean_search_query(query: str) -> str:
    """
    Clean the search query by removing non-alphanumeric characters and extra spaces.
    """
    query = query.lower().strip()
    
    cleaned = ""
    for char in query:
        if char.isalnum() or char.isspace():
            cleaned += char

    return " ".join(cleaned.split())


def find_word_positions(sentence_words: list, query_words: list) -> list:
    """
    Finds the starting word positions of a query within a single sentence's word list.
    Position numbering starts from 1.
    """
    positions = []
    query_len = len(query_words)
    
    # Slide across the individual words of this sentence
    for i in range(len(sentence_words) - query_len + 1):
        if sentence_words[i : i + query_len] == query_words:
            positions.append(i + 1) # 1-based index positioning

    return positions


def search_in_document(document: TextDocument, query: str) -> list:
    """
    Searches the TextDocument structure for exact words/phrases.
    Returns a list of dictionaries with matching structural details.
    """
    cleaned_query = clean_search_query(query)

    if cleaned_query == "" or document.is_empty():
        return []
    
    query_words = cleaned_query.split()
    results = []

    # Iterate through the document's sentences (where each sentence is a list of words)
    for index, sentence_words in enumerate(document.sentences, start=1):
        
        # Calculate matching indices inside this specific sentence
        positions = find_word_positions(sentence_words, query_words)
        
        # Only log a match if the phrase/word actually exists as independent tokens
        if positions:
            sentence_text = " ".join(sentence_words)
            result = {
                "sentence_number": index,
                "sentence": sentence_text,
                "positions": positions
            }
            results.append(result)

    return results


def print_search_results(results: list, query: str) -> None:
    """Prints the formatted matching locations out to the terminal interface."""
    cleaned_query = clean_search_query(query)
    
    if len(results) == 0:
        print(f"\nNo results found for: '{cleaned_query}'")
        return
        
    print(f"\nSearch results for: '{cleaned_query}'")
    print("-" * 40)

    for result in results:
        print(f"Sentence Number: {result['sentence_number']}")
        print(f"Sentence       : {result['sentence']}")
        print(f"Word Positions : {result['positions']}\n")


def search_prompt(document: TextDocument) -> None:
    """Interactive loop tracking user sub-menu queries."""
    while True:
        query = input("\nEnter a word or phrase to search, or type 'q' to quit: ").strip()

        if query.lower() == "q":
            print("Search operation finished.")
            break

        results = search_in_document(document, query)
        print_search_results(results, query)