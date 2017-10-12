patterns = [(r'.*ing$', 'VBG'), (r'.*ed$', 'VBD'), (r'.*es$', 'VBZ'), (r'.*ould$', 'MD'), (r'.*\'s$', 'NN$'),
             (r'.*s$', 'NNS'),  (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), (r'.*', 'NN')]

# explanation for each tuple

import nltk

regexp_tagger = nltk.RegexpTagger(patterns)
print(regexp_tagger.tag(nltk.corpus.brown.words()))
