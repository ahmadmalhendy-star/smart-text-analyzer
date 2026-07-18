class Dashboard:

    def __init__(self, text):
        self.text = text

    def show_dashboard(self):
        words = self.text.split()

        total_words = len(words)

        unique_words = len(set(words))

        text_without_spaces = self.text.replace(" ", "")

        total_characters = len(text_without_spaces)

        char_count = {}

        for char in text_without_spaces:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        print("\n========== DASHBOARD ==========")
        print(f"Total Words      : {total_words}")
        print(f"Unique Words     : {unique_words}")
        print(f"Total Characters : {total_characters}")

        print("\nCharacter Frequency:")
        for char, count in char_count.items():
            print(f"{char} : {count}")

        print("==============================")


text = input("Enter your text: ").lower()

dashboard = Dashboard(text)
dashboard.show_dashboard()
