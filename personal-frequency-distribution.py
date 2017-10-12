from nltk.book import *


text = 'Hello ! This is a course designed for people who are interested in learning the core concepts of NLP and ' \
       'utilise those concepts to make applications like sentiment analysis make make'
distribution = FreqDist(text.split(' '))
words = distribution.keys()
print(words)

print(list(words)[:3])
print(distribution['make'])
