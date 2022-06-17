# Ask dozie for input
my_sentence = input("Enter a sentence: ")

# Remove extra whitespace
my_sentence = my_sentence.strip(" ")

# Split the sentence into words
list_of_words = my_sentence.split(" ")

# Count the number of words
number_of_words = len(list_of_words)

# Print the number of words
print(number_of_words)

