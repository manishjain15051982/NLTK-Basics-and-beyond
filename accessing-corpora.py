import nltk


# some names of the corpus provided in the nltk module are listed below
# Gutenberg Corpus - import format --> nltk.corpus.gutenberg
# Web and Chat Text - import format --> nltk.corpus.webtext
# NPS Chat - import format --> nltk.corpus.nps_chat
# Brown Corpus - import format --> nltk.corpus.brown
# Reuters Corpus - import format --> nltk.corpus.reuters
# Inaugural Address Corpus - import format --> nltk.corpus.inaugural

from nltk.corpus import gutenberg

print(gutenberg.fileids())

bible_kjv = gutenberg.words('bible-kjv.txt')
print(len(bible_kjv))
print(bible_kjv,'\n\n\n')

# functions - raw() - words() - sents()

for fileid in gutenberg.fileids():
   num_chars = len(gutenberg.raw(fileid))
   num_words = len(gutenberg.words(fileid))
   num_sents = len(gutenberg.sents(fileid))
   vocabulary = set([w.lower() for w in gutenberg.words(fileid)])
   print('Data for File Id :',fileid)
   print('Number of characters:',num_chars,'\nNumber of words:',num_words,'\nNumber of sentences:',num_sents)
   print('Vocabulary:\n',vocabulary,'\n\n\n')
