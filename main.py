from menu import display_menu
from core.text_loader import initial_text_input_prompt
from core.text_processor import process_document
from core.dashboard import generate_dashboard
from core.search import search_prompt 
from core.replace import replace_word
from Features.keywords import keyword_extraction
from Features.sentiment import analyze_sentiment 
from Features.undo_redo import UndoRedoManager
from Features.text_auto_completion import autocomplete_prompt
from Models.text_document import TextDocument
if __name__ == "__main__":
    choice = display_menu()
    manager = UndoRedoManager()
    current_text = ""
    doc = TextDocument()
    while choice != "10":
        if choice == "1":
            metrics = generate_dashboard(doc, top_n_chars=5)
            
            print(f"\n--- Consolidated Analytics Dashboard ---")
            if not doc.raw_text:
                print("No text available. Please insert text first.")
            else:
                print(f"Current Text       :\n{ '#' * 50 }\n{doc.raw_text}\n{ '#' * 50 }\n")
            print(f"Total Word Count   : {metrics['total_words']}")
            print(f"Unique Word Count  : {metrics['unique_words']}")
            print(f"Total Characters   : {metrics['total_characters']} (excluding spaces)")
            
            print("\nCharacter Frequencies (Top 5):")
            for char, count in metrics['top_characters']:
                print(f"  • '{char}': {count}x")
            choice = display_menu()


        elif choice == "2":
            doc.raw_text = initial_text_input_prompt()
            print(f"Text inserted successfully.\n{doc.raw_text}")
            process_document(doc)
            manager.save_state(current_text)
            current_text = doc.processed_text
            choice = display_menu()


        elif choice == "3":
            search_prompt(doc)
            choice = display_menu()


        elif choice == "4":
            autocomplete_prompt(doc)
            choice = display_menu()


        elif choice == "5":
            sentiment_label, positive_count, negative_count = analyze_sentiment(doc.processed_text)
            print(f"\nSentiment Analysis Result:")
            print(f"  Sentiment: {sentiment_label}")
            print(f"  Positive Words Count: {positive_count}")
            print(f"  Negative Words Count: {negative_count}")
            choice = display_menu()


        elif choice == "6":
            top_keywords = keyword_extraction(doc.processed_text, top_n=5)            
            print("\nTop 5 Keywords Extracted (excluding structural fillers):")
            if not top_keywords:
                print("  No meaningful keywords found.")
            for keyword, frequency in top_keywords:
                print(f"  ★ {keyword} (Occurrences: {frequency}x)")
            choice = display_menu()

        elif choice == "7":
            old_word = input("Enter the word to replace: ").strip()
            new_word = input("Enter the new word: ").strip()
            
            # Run the replacement logic
            updated_text = replace_word(doc.raw_text, old_word, new_word)
            
            if updated_text == doc.raw_text:
                print(f"\nNo standalone occurrences of '{old_word}' were found to replace.")
            else:
                # 1. SAVE THE OLD STATE FIRST (Crucial for Undo to function properly)
                manager.save_state(doc.raw_text)
                
                # 2. Update the raw text payload
                doc.raw_text = updated_text
                
                # 3. RE-PROCESS THE ENTIRE DOCUMENT (Updates words, sentences, and vocabs lists)
                process_document(doc)
                
                print(f"\nSuccess: Replaced '{old_word}' with '{new_word}'.")
            choice = display_menu()

        elif choice == "8":
            print("Undo selected.")
            previous_text = manager.undo(current_text)
            if previous_text == current_text:
                print("Nothing to undo!")
            else:
                print(f"Undo performed! Reverted to: {previous_text}")
                current_text = previous_text
            choice = display_menu()


        elif choice == "9":
            print("Redo selected.")
            next_text = manager.redo(current_text)
            if next_text == current_text:
                print("Nothing to redo!")
            else:
                print(f"Redo performed! Advanced to: {next_text}")
                current_text = next_text
            choice = display_menu()


        elif choice == "9":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


