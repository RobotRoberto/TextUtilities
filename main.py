import pronouncing as pn
import spacy
from PyDictionary import PyDictionary
from pprint import pprint

test_string = "And our nation itself is testimony to the love our veterans have had for it and for us. All for which America stands is safe today because brave men and women have been ready to face the fire at freedom's front."

nlp = spacy.load('en')

tokenized = nlp(test_string)

print("This is the tokenized sentence.\n")

print(tokenized)

nlp.vocab[tokenized[-2].lemma].is_stop = False

filtered = [x for x in tokenized if not x.is_stop]

print("\nThis is after removing stop words.\n")

print(filtered)

first_sounds = []
alliteration_dict = dict()

for index in range(len(filtered)):
    word = filtered[index]
    word_pron = pn.phones_for_word(word.text)

    if (len(word_pron) > 0):
        leading_sound = word_pron[0].split(" ")[0]
        first_sounds.append(leading_sound)

        if leading_sound not in alliteration_dict:
            alliteration_dict[leading_sound] = [word]
        else:
            alliteration_dict[leading_sound].append(word)

print ("\nThis is all of the first pronounciations of the sentence.\n")

print(first_sounds)

alliteration_list = []

for key, value in alliteration_dict.items():
    sort_list = []

    for token in value:
        if len(sort_list) == 0:
            sort_list.append(token)
        elif token.i - sort_list[len(sort_list) - 1].i < 5:
            sort_list.append(token)
        else:
            sort_list = [token]

    if len(sort_list) > 1:
        alliteration_list.append(sort_list)

print("\nThis is a list of lists of possible alliterations.\n")
for x in alliteration_list:
    print(x)

dictionary = PyDictionary()
antonyms = set()

for word in filtered:
    antonyms_word = dictionary.antonym(word.lemma_)
    if antonyms_word is not None:
        for other in filtered:
            if other.lemma_ in antonyms_word and (other, word) not in antonyms:
                antonyms.add((word, other))


print("\n\nSet of antonyms within the sentence")
pprint(antonyms)
