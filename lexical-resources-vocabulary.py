import nltk
from nltk.corpus import gutenberg


def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)


list_of_unusual_words = unusual_words(gutenberg.words('austen-sense.txt'))
print(list_of_unusual_words)


# stop words

from nltk.corpus import stopwords


#print(stopwords.words('english'))