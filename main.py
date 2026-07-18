from menu import display_menu
from core.text_loader import initial_text_input_prompt
from core.text_processor import process_document
from Features.undo_redo import UndoRedoManager
from Models.text_document import TextDocument
if __name__ == "__main__":
    choice = display_menu()
    doc = TextDocument()
    while choice != "8":
        if choice == "1":
            print("Dashboard selected.")
        elif choice == "2":
            doc.raw_text = initial_text_input_prompt()
            print(f"Text inserted successfully.\n{doc.raw_text}")
            process_document(doc)
            print(f"Processed Text: {doc.processed_text}")
        elif choice == "3":
            print("Search selected.")
        elif choice == "4":
            print("Autocomplete selected.")
        elif choice == "5":
            print("Sentiment Analysis selected.")
        elif choice == "6":
            print("Undo selected.")
        elif choice == "7":
            print("Redo selected.")
        else:
            print("Invalid choice. Please select a valid option.")


