import nltk

sentence = "The smart student solved the problem"
tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)

grammar = "NP: {<DT><JJ><NN>}"
parser = nltk.RegexpParser(grammar)
tree = parser.parse(tags)

for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        print(subtree)
