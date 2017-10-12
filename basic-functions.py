from nltk.book import *

print('\n\n\n')

# BASIC FUNCTIONS FOR SEARCHING TEXT

# concordance function  - inputs --> a single word to search
#                       - outputs--> every occurrence of the word together with some context

#text1.concordance("man")

print('\n\n\n')

# similar function - inputs --> a single word to search
#                  - outputs--> all other words which appear in the context of the word provided in the input

#text1.similar('woman')

print('\n\n\n')

# common_contexts function - inputs --> a list of words
#                          - outputs--> all the contexts shared by the list of words provided in the input together

#text4.common_contexts(['bad','very'])

print('\n\n\n')

# dispersion plot - a graph of texts with the given list of words showing their positions in the text with their
#                   frequency graphically

#text4.dispersion_plot(['citizen','democracy','freedom'])

# Counting words in the text

# function -- len()

#print(len(text4))

print('\n\n\n')

# count the occurrence of a particular word in the text

#print(text4.count('freedom'))

# we can calculate the percentage of a word occurring in the text

#print(100 * (text4.count('freedom')/len(text4)))

print('\n\n\n')




