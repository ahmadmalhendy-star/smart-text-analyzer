from Features.undo_redo import UndoRedoManager
from Features.text_auto_completion import autocomplete_prompt
from Models.text_document import TextDocument
from core.text_processor import process_document
def display_menu():
    manager = UndoRedoManager()
    current_text = ""
    document=TextDocument()
    while True:
        print("\n" + "="*30)
        print("    SMART TEXT ANALYZER    ")
        print("="*30)
        print(f"Current Text: '{current_text}'")
        print("-"*30)
        print("1. Insert/Update Text")
        print("2. Undo Action")
        print("3. Redo Action")
        print("4.Auto complition")
        print("5. Exit")
        print("="*30)
        
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            new_text = input("Enter new text: ")
            # Save the old state before updating
            manager.save_state(current_text)
            current_text = new_text
            document=TextDocument()
            document.raw_text=current_text
            process_document(document)
            print("Text updated successfully!")

        elif choice == "2":
            previous_text = manager.undo(current_text)
            if previous_text == current_text:
                print("Nothing to undo!")
            else:
                current_text = previous_text
                print("Undo performed!")

        elif choice == "3":
            next_text = manager.redo(current_text)
            if next_text == current_text:
                print("Nothing to redo!")
            else:
                current_text = next_text
                print("Redo performed!")

        elif choice == "4":
           if current_text.strip() == "":
               print("Please insert text first!")
           else:
             autocomplete_prompt(document)

        elif choice == "5":
           print("Exiting application. Goodbye!")
           break

        else:
           print("Invalid choice! Please select between 1-5.")


        
