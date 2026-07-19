def keyword_extraction(text, top_n: int = 5) -> list:
    """
    Extracts keywords from the given text using a simple frequency-based approach"""

    STOP_WORDS = {
        "the", "a", "an", "and", "or", "but", "is", "are", "was", "were", 
        "to", "of", "in", "on", "at", "by", "for", "with", "about", "i", 
        "you", "it", "this", "that", "can", "we", "he", "she", "they", "have"
    }

    #  Filter out stop words and count the frequency of remaining words
    filtered_words = [word.lower() for word in text.split() if word.lower() not in STOP_WORDS]
    word_freq = {}
    for word in filtered_words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Sort the words by frequency in descending order and return the top N keywords
    sorted_keywords = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)

    return sorted_keywords[:top_n]