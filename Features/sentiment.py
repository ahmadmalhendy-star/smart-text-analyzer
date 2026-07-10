
import re

# Positive and negative lexicons (can be expanded)
POSITIVE_WORDS = {
    "good", "great", "excellent", "amazing", "awesome",
    "happy", "love", "like", "wonderful", "best",
    "fantastic", "nice", "perfect", "enjoy", "success"
}

NEGATIVE_WORDS = {
    "bad", "terrible", "awful", "poor", "hate",
    "worst", "sad", "angry", "problem", "failure",
    "horrible", "disappointing", "ugly", "difficult"
}

NEGATIONS = {
    "not", "no", "never", "n't"
}


def tokenize(text:str) -> list[str]:
    """
    Convert text into lowercase words.
    """
    return re.findall(r"\b[\w']+\b", text.lower())
def analyze_sentiment(text:str) -> tuple[str, int, int]:
    """
    Analyze the sentiment of the given text.
    
    Returns:
        sentiment (str): 'positive', 'negative', or 'neutral'
        positive_count (int): Number of positive words
        negative_count (int): Number of negative words
    """
    positive = 0
    negative = 0
    words = tokenize(text)

    for i,word in enumerate(words):
        negated = i > 0 and words[i -  1] in NEGATIONS
        if negated:
            if word in POSITIVE_WORDS:
                negative += 1
            elif word in NEGATIVE_WORDS:
                positive += 1
        else:
            if word in POSITIVE_WORDS:
                positive += 1
            elif word in NEGATIVE_WORDS:
                negative += 1
        
    if positive > negative:
        label = "Positive 😊"
    elif negative > positive:
        label = "Negative ☹️"
    else:
        label = "Neutral 😐"
    return label, positive, negative
