from nltk.corpus import brown
import nltk


brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
print(unigram_tagger.tag(nltk.word_tokenize('We are using the programming language Python')))

print(unigram_tagger.tag(brown_sents[1005]))


# evaluation function -- evaluate()
print(unigram_tagger.evaluate(brown_tagged_sents))


# separating training and testing data

size = int(len(brown_tagged_sents) * 0.9)
train_sentences = brown_tagged_sents[:size]
test_sentences = brown_tagged_sents[size:]
unigram_tagger = nltk.UnigramTagger(train_sentences)
#print(unigram_tagger.evaluate(test_sentences))

print(unigram_tagger.tag(nltk.word_tokenize('We are using the programming language Python')))

