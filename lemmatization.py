from nltk import WordNetLemmatizer
from nltk.corpus import brown
import nltk

# Difference between stemming and lemmatization

tokens = brown.words(categories=['religion'])
wnl = WordNetLemmatizer()
print([wnl.lemmatize(t) for t in tokens])

# The WordNet lemmatizer only removes affixes if the resulting word is in its dictionary
# It is a good choice if you want to compile the vocabulary of some texts and want a list of valid lemmas

tokens = nltk.word_tokenize('the women are lying')
print([wnl.lemmatize(t) for t in tokens])

# converted women to woman but was unable to convert lying to lie
