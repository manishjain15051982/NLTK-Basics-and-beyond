# Introduction to tagger

import nltk

text = 'We are learning Natural Languages Processing'

tokens = nltk.word_tokenize(text)
print(nltk.pos_tag(tokens))

# what is pos_tag function returning ?
# Guide to each tag

print(nltk.help.upenn_tagset('PRP'))

# You can also use the nltk module for documentation purposes as shown above


# similar method of text

text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print(text.similar('woman'))

# explanation

print(text.similar('bought'))
