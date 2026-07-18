from Models.text_document import TextDocument

#clean the search
def clean_search_query(query:str) ->str:
    query=query.lower().strip()

    cleaned=""
    for char in query:
        if char.isalnum () or char.isspace():
             cleaned+=char

    cleaned=" ".join(cleaned.split())

    return cleaned 

def find_word_positions(sentence_words: list, query: str) -> list:
    """
    Find the word position inside the sentence.
    Position starts from 1.
    """
    positions = []

    query_words = query.split()

    for i in range(len(sentence_words)):
        if sentence_words[i:i + len(query_words)] == query_words:
            positions.append(i + 1)

    return positions





#search for a word 
def search_in_document (document:TextDocument,query:str) ->str:
    query=clean_search_query(query)

    if query=="":
        return []
    if document.is_empty():
        return []
    
    results = []

    for index,sentence_word in enumerate(document.sentences,start=1):
        sentence_text=" ".join(sentence_word)
        if query in sentence_text:
            positions = find_word_positions(sentence_word, query)
            result={"sentence_number ":index,
                    "sentence":sentence_text,
                    "positions":positions


         }
            
            results.append(result)

    return results

def print_search_results(results:list, query:str) ->str:
   """
    print the result 
   """
   if len(results)==0:
       print(f"\nNo results found :{query} ")
       return
   print(f"\nsearch result for :{query} ")
   print("-"*40)

   for result in results :
       print(f"sentenc number:{result['sentence_number ']}")
       print(f"sentece:{result['sentence']}")
       print(f"Word positions:{result['positions']}")

def search_prompt(document: TextDocument) -> None:
    '''
    user search many item
    '''
    while True:
        query=input("\nEnter a word or phrase to search, or type 'q' to quit :").strip()

        if query.lower()=="q":
            print(" the search finish")
            break

        results = search_in_document(document, query)
        print_search_results(results, query)
   
      


from Models.text_document import TextDocument
from core.text_loader import initial_text_input_prompt
from core.text_processor import process_document


def main():
    raw_text = initial_text_input_prompt()

    if raw_text == "":
        print("No text entered.") 
        return

    document = TextDocument()
    document.raw_text = raw_text

    process_document(document)

    search_prompt(document)


if __name__=="__main__":
    main()




