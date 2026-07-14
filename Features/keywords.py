class TextProcessor:
    def __init__(self, text):
        self.text = text

    def keyword_extraction(self):
        stop_words = ["the", "is", "a", "an", "and", "or", "to", "of", "in"]
        words = self.text.split()
        keywords = []

        for word in words:
            if word not in stop_words:
                keywords.append(word)

        printed = []
        print("\nKeywords:\n")

        for word in keywords:
            if word not in printed:
                count = 0
                for w in keywords:
                    if w == word:
                        count += 1
                print(word, ":", count)
                printed.append(word)



 
my_text = input("Enter your text: ")


processor = TextProcessor(my_text)


processor.keyword_extraction()

