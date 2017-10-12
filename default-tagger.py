from nltk.corpus import brown
import nltk


tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
print(nltk.FreqDist(tags).max())

raw_text = 'We are learning taggers right now and aim to build applications which uses language to perform analysis'
tokens = nltk.word_tokenize(raw_text)
default_tagger = nltk.DefaultTagger(nltk.FreqDist(tags).max())
print(default_tagger.tag(tokens))

# surprisingly poor performance

