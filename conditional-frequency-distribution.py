from nltk.corpus import brown


# Introduction to the Brown Corpus

print(brown.categories())

# Accessing words of Brown Corpus

print(brown.words(categories='adventure'))

# Introduction to Conditional Frequency Distribution

from nltk import ConditionalFreqDist

pair_list = [(genre,word) for genre in brown.categories() for word in brown.words(categories=genre)]


cfd = ConditionalFreqDist(pair_list)
genres = ['news', 'romance', 'religion', 'humor']
modals = ['it', 'could', 'may', 'might', 'must']

cfd.tabulate(conditions=genres, samples=modals)

# conditions method

print(cfd.conditions())

print(cfd['romance']['could'])
