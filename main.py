from core.replace import replace_word

if __name__ == "__main__":
    current_text = ""
    
    while True:
        print("\n" + "="*30)
        print("  SMART TEXT ANALYZER  ")
        print("="*30)
        print(f"Current Text: '{current_text}'")
        print("-"*30)
        print("1. Insert/Update Text")
        print("2. Undo Action")
        print("3. Redo Action")
        print("4. Exit")
        print("5. Replace Word")  # أضفناها مباشرة هنا ل تظهر بالتأكيد
        print("="*30)
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            current_text = input("Enter new text: ")
            print("Text updated successfully!")
        elif choice == "5":
            old_w = input("Enter the word to replace: ")
            new_w = input("Enter the new word: ")
            current_text = replace_word(current_text, old_w, new_w)
            print("Text updated successfully!")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Feature coming soon or invalid option!")