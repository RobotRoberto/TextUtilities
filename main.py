import spacy
from pprint import pprint
from TextUtilities import TextUtilities

test_string = "And our nation itself is testimony to the love our veterans have had for it and for us. All for which America stands is safe today because brave men and women have been ready to face the fire at freedom's front."

nlp = spacy.load('en')

tokenized = nlp(test_string)

print("This is the tokenized sentence.\n")

print(tokenized)

nlp.vocab[tokenized[-2].lemma].is_stop = False

filtered = [x for x in tokenized if not x.is_stop]

print("\nThis is after removing stop words.\n")

print(filtered)

util = TextUtilities()

alliteration_list = util.findAlliteration(filtered, logging=True)

antonyms = util.findAntonymPairs(filtered)

print("\n\nSet of antonyms within the sentence")
pprint(antonyms)