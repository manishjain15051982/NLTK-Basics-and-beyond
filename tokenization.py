from nltk.tokenize import word_tokenize, sent_tokenize

# INTRODUCTION


def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

text = read_file('shakespeare-taming-of-the-shrew.txt')

# word_tokenize - inputs ---> string containing the text
#               - outputs --> list of words


words = word_tokenize(text)
#print(words)
#print('size as list :', len(words))
#print('size as set : ', len(set(words)))

# sent_tokenize - inputs ---> string containing the text
#               - outupts --> list of sentences

sentences = sent_tokenize(text)
for sentence in sentences:
  print(sentence)