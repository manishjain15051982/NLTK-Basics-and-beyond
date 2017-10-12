from nltk.book import *


print('\n\n\n')
distribution_1 = FreqDist(text1)
print(distribution_1,'\n\n')

words = distribution_1.keys()
print(type(words))
print(words)
words_list = list(words)
print(words_list[:10])

print(distribution_1['whale'])

# plot function

distribution_1.plot(50)