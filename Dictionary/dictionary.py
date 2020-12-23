from PyDictionary import PyDictionary
import pprint

# creating a dictionary instance
dict = PyDictionary()

# taking input from the user: the word and letter for specified action needed by the user
word = input("Please enter a word: ")
action = input("""\nWhat do you want to find? a. meaning b. synonyms c. antonyms.
Please enter a letter: """)

# performing specified action needed based on user input
if action == 'a' or action == 'A':
    meaning = dict.meaning(word)
    print("\nThe meaning of the word " + word.upper() + "\n\n")
    pprint.pprint(meaning)

elif action == 'b' or action == 'B':
    synonymns = dict.synonym(word)
    print("\nSynonymns for the word " + word.upper() + "\n\n")
    pprint.pprint(synonymns)

elif action == 'c' or action == 'C':
    antonyms = dict.antonym(word)
    print("\nAntonyms for the word " + word.upper() + "\n\n")
    pprint.pprint(antonyms)
