import sys
from stats import count_words
from stats import character_count
from stats import sorted_dict
if len(sys.argv) < 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def  main ():
    filepath = sys.argv[1]
    contents = get_book_text (filepath)
    num_words = count_words(contents)
    character_dict = character_count (contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #loop through and format each character here
    num_characters = sorted_dict(character_dict)
    for char_dict in num_characters:
        if char_dict["char"].isalpha(): #only print alphabetical characters
            print(f'{char_dict["char"]}: {char_dict["num"]}')
    print ("============= END ===============")

main()
