class SmartTextAnalyzer:

    def main(self):

        while True:

            print("\n===== Smart Text Analyzer =====")
            print("1. Dashboard")
            print("2. Search")
            print("3. Replace Word")
            print("4. Keyword Extraction")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1": #dashboard
                print("Dashboard selected")

            elif choice == "2": #search
                print("Search selected")

            elif choice == "3": #replace
                print("Replace Word selected")

            elif choice == '4':
                # 1. فتح القائمة الفرعية للميزات الذكية عند اختيار رقم 4
                while True:
                    print("\n" + "-"*40)
                    print("     SMART FEATURES SUBMENU      ")
                    print("-"*40)
                    print("1. Text Sentiment Analysis (تحليل المشاعر)")
                    print("2. Keyword Extraction (الكلمات المفتاحية)")
                    print("3. Text Auto-Completion (الإكمال التلقائي)")
                    print("4. Undo/Redo Replacements (التراجع والإعادة)")
                    print("5. Back to Main Menu (العودة للقائمة الرئيسية)")
                    print("-"*40)
                    
                    sub_choice = input("Select a smart feature (1-5): ").strip()
                    
                    # ربط كل ميزة ذكية بملفها المخصص في مجلد Features
                    if sub_choice == '1':
                        analyze_sentiment(master_text)       # ملف sentiment.py
                    elif sub_choice == '2':
                        extract_keywords(master_text)        # ملف keywords.py
                    elif sub_choice == '3':
                        run_auto_complete(master_text)       # ملف text_auto_completion.py
                    elif sub_choice == '4':
                        print("تفعيل ميزة التراجع والإعادة...") # ملف undo_redo.py
                    elif sub_choice == '5':
                        print("Returning to main menu...")
                        break # كسر اللوب الفرعية والرجوع للقائمة الأساسية
                    else:
                        print(" Invalid choice! Please enter a number between 1 and 5.")
                    print("Keyword Extraction selected")

            elif choice == "5":
                print("Thank you!")
                break

            else:
                print("Invalid choice, try again.")

programe= SmartTextAnalyzer()
programe.main()
