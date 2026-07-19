# ()
import re 

from Models.text_document import TextDocument

def process_text(text: str) -> str:
    """
    Normalize the input text by:
    - converting to lowercase
    - removing punctuation
    - removing extra whitespace
    """
    text = text.lower()
    text = re.sub(r'[^\w\s.!?]', '', text) # Remove punctuation except for sentence-ending punctuation
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def split_into_sentences(text: str) -> list:
    """
    Split the text into sentences.
    """
    sentence_strings = re.split(r"[.!?]+", text)
    return [sentence.strip() for sentence in sentence_strings if sentence.strip()]

def tokenize(sentence: str) -> list:
    """
    Tokenize a sentence into words.
    """
    return sentence.split()

def process_document(document: TextDocument) :
    """
    Process the input text and return a TextDocument object containing
    the raw text, processed text, sentences, words, and unique vocabulary.
    """
    processed = process_text(document.raw_text)
    sentence_strings  = split_into_sentences(processed)
    sentences = []
    for sentence in sentence_strings:
        sentences.append(tokenize(sentence))
    words = processed.split()
    vocabs = set(words)
    document.updated_text(new_text=document.raw_text,
                          processed_text=processed,
                          sentences=sentences,
                          words=words,
                          vocaps=vocabs)