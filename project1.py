def count_word_occurences(mystr):
    # We use lower function so that "This" matches with "this" 
    # Basically we ignore the uppercase and lowercase characters and focus on matching the words
    mystr = mystr.lower()
    punctuation_marks = '''!@#$%^&*()_+=-{}[]<>/,.?~'":;'''
    # Iterating through all the punctuation and finding thme in the myr and replacing those with nothing
    for char in punctuation_marks:
        mystr = mystr.replace(char, "")
    
    # Converting the string into list of words by spliting the string by spaces
    words = mystr.split()

    # Unique_words list will contain all the unique words from mystr
    unique_words = []

    # Words_counts list will contain the frequency of every unique word in mystr
    word_counts = []

mystr = input("Please enter a string: ")
words, counts = count_word_occurences(mystr)

print("word occurences:")

# When we want to loop trough two lists, two tuples, two strings together then we use zip and put them in zip function
for word, count in zip(words, counts):
    print(f"{word}:{count} times")