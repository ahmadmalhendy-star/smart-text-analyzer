from Features.undo_redo import UndoRedoManager

def display_menu():
    print("\n" + "="*30)
    print("    SMART TEXT ANALYZER    ")
    print("="*30)
    print("1. Dashboard")
    print("2. Insert Text")
    print("3. Search")
    print("4. Autocomplete")
    print("5. Sentiment Analysis")
    print("6. Undo")
    print("7. Redo")
    print("8. Exit")
    print("="*30)
    choice = input("Select an option (1-8): ").strip()
    return choice
    # manager = UndoRedoManager()
    # current_text = ""

    # while True:
    #     print("\n" + "="*30)
    #     print("    SMART TEXT ANALYZER    ")
    #     print("="*30)
    #     print(f"Current Text: '{current_text}'")
    #     print("-"*30)
    #     print("1. Insert/Update Text")
    #     print("2. Undo Action")
    #     print("3. Redo Action")
    #     print("4. Exit")
    #     print("="*30)
        
    #     choice = input("Select an option (1-4): ").strip()

    #     if choice == "1":
    #         new_text = input("Enter new text: ")
    #         # Save the old state before updating
    #         manager.save_state(current_text)
    #         current_text = new_text
    #         print("Text updated successfully!")

    #     elif choice == "2":
    #         previous_text = manager.undo(current_text)
    #         if previous_text == current_text:
    #             print("Nothing to undo!")
    #         else:
    #             current_text = previous_text
    #             print("Undo performed!")

    #     elif choice == "3":
    #         next_text = manager.redo(current_text)
    #         if next_text == current_text:
    #             print("Nothing to redo!")
    #         else:
    #             current_text = next_text
    #             print("Redo performed!")

    #     elif choice == "4":
    #         print("Exiting application. Goodbye!")
    #         break
    #     else:
    #         print("Invalid choice! Please select between 1-4.")
