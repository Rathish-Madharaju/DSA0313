from nltk.corpus import wordnet as wn

word = "bank"
synsets = wn.synsets(word)

for s in synsets[:3]:
    print(s.name(), ":", s.definition())
