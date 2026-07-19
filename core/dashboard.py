# core/dashboard.py
from Models.text_document import TextDocument

def generate_dashboard(doc: TextDocument, top_n_chars: int = 5) -> dict:
    """
    Generates a dictionary of text metrics for the dashboard view,
    including word counts, unique vocabulary size, and top character frequencies.
    """
    # 1. Calculate basic counts
    total_words = len(doc.words)
    unique_words = len(doc.vocaps)
    
    # 2. Strip all whitespace to calculate true character count
    no_spaces = "".join(doc.raw_text.split())
    total_chars = len(no_spaces)
    
    # 3. Compute character distributions (case-insensitive)
    char_counts = {}
    for char in no_spaces.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # 4. Sort characters by frequency descending
    sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    top_characters = sorted_chars[:top_n_chars]
    
    # 5. Return structured payload
    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "total_characters": total_chars,
        "top_characters": top_characters
    }