
# ()

class TextDocument:
    """
    Manages the state of the loaded document, including raw text, 
    tokenized words, and structured sentences.
    """
    def __init__(self):
        self.raw_text = ""
        self.processed_text = ""
        self.sentences = []     # List of lists (sentences containing words)
        self.wrods = []         # Flat list of all words
        self.vocaps = set()     # Set of unique words for O(1) lookups

    def updated_text(self,
            new_text: str,
            processed_text: str,
            sentences: str,
            wrods: str,
            vocaps: str):
        self.raw_text = new_text
        self.processed_text = processed_text
        self.sentences = sentences
        self.wrods = wrods
        self.vocaps = set(vocaps)
    def is_empty(self):
        return not self.raw_text