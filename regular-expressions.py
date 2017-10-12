from nltk.tokenize import word_tokenize
import re


def read_file(filename):
    with open(filename,'r') as file:
        text = file.read()
    return text

text = read_file('shakespeare-taming-of-the-shrew.txt')

words = word_tokenize(text)


# search function

# example - get all words which end with ed

#print([w for w in words if re.search('ing$',w)])


# ranges and closures
# *, +

#print([w for w in words if re.search('^a+',w)])
print([w for w in words if re.search('^b[a-z]*t$',w)])


