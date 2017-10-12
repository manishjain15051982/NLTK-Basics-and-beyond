from nltk import PorterStemmer, LancasterStemmer
import nltk


tokens = nltk.corpus.brown.words(categories=['romance'])

# off the shelf stemmers

# The Porter Stemmer is a good choice if you are indexing some texts and want to support search using alternative forms
# of words

porter = PorterStemmer()
# stem() function - takes a token as input
print([porter.stem(t) for t in tokens])

lancaster = LancasterStemmer()
print([lancaster.stem(t) for t in tokens])