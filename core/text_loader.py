import os

def load_from_terminal() -> str:
    """
        Reads multi-line from the terminal until the user enter '$$END_TEXT$$' 
    """
    print("\nEnter/Paste your text below. Type '$$END_TEXT$$' on a new line to finish")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "$$END_TEXT$$":
                break
            lines.append(line)
        except EOFError:
            break
    return "\n".join(lines)

def load_from_file() -> str:
    """
        Prompt the user to enter a valid local file path and reads its content.
    """
    path = input("\nEnter the full path to the local text file (or enter 'q' for cancel): ").strip()
    if path.lower() == "q":
        return ""
    if os.path.exists(path) and os.path.isfile(path):    
        try:
            with open(path) as file:
                return file.read()
        except Exception as e:
            print(f"❌ Error reading file: {e}. Please try again.")
    else:
        print("❌ File not found. Please ensure the path is correct.")

def initial_text_input_prompt() -> str:
    """
    The main landing prompt routing the user to their preferred input method.
    """
    print("=" * 50)
    print("Welcome to the Smart Text Analyzer!") 
    print("=" * 50)
    print("1. Direct Text Entry (Type/Paste into terminal)")
    print("2. File Path Input (Load from a .txt file)")
    
    while True:
        choice = input("\nSelect an input method (1 or 2): ").strip()
        if choice == '1':
            return load_from_terminal()
        elif choice == '2':
            text = load_from_file()
            if text:  # If user didn't cancel
                return text
        else:
            print("❌ Invalid selection. Please enter 1 or 2.")