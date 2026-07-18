

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
