from nltk.corpus import gutenberg, brown
import nltk


#moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
#print(moby.findall(r'<a><.*><.*man>'))


hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
print(hobbies_learned.findall(r'<\w*><and><other><\w*s>'))

# passing your own list of words

text = 'Hello, I am a computer programmer who is currently learning and studying NLP !'

obj = nltk.Text(nltk.word_tokenize(text))
#print(obj.findall(r'<.*><.*><.*ed>+'))
