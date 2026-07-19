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
    print("6. Keyword Extraction")
    print("7. Replace Word")
    print("8. Undo")
    print("9. Redo")
    print("10. Exit")
    print("="*30)
    choice = input("Select an option (1-10): ").strip()
    return choice
    