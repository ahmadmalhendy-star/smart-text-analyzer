
from Models.text_document import TextDocument
from core.text_loader import initial_text_input_prompt
from core.text_processor import process_document
from core.search import search_prompt
from Features.text_auto_completion import autocomplete_prompt


def main():
    raw_text = initial_text_input_prompt()

    if raw_text == "":
        print("No text entered.")
        return

    document = TextDocument()
    document.raw_text = raw_text

    process_document(document)

    while True:
        print("\nMain Menu")
        print("1. Search")
        print("2. Smart Autocompletion")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            search_prompt(document)

        elif choice == "2":
            autocomplete_prompt(document)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()