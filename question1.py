""" Question 1 Write a program to compute the frequency of the words from the input. """
str = input("Enter the required string: ")
word_counts = dict()
for str in str.split():
    if str in word_counts:
        word_counts[str] = word_counts[str] + 1
    else:
        word_counts[str] = 1
final_word = sorted(tuple(list(word_counts.items())))
for item in final_word:
    print(item)

