import pronouncing as pn
import spacy
from PyDictionary import PyDictionary

"""
Utilities class to find a limited set of figurative language components
"""
class TextUtilities:	
	
	"""
	Initializes the class. 
	"""
	def __init__(self):
		self.dictionary = PyDictionary() 

	"""
	Finds all of the pronounciation for first syllables in tokenized document.
	There will be logging of things happening.
	"""
	def __findFirstSyllableLogging(self, tokenized_doc):
		first_sounds = []
		alliteration_dict = dict()

		for index in range(len(tokenized_doc)):
			word = tokenized_doc[index]
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
		return alliteration_dict
		
	"""
	Finds all of the pronounciation for first 	syllables in tokenized document.\
	No logging will be provided.
	"""
	def __findFirstSyllable(self, tokenized_doc):
		alliteration_dict = dict()

		for index in range(len(tokenized_doc)):
			word = tokenized_doc[index]
			word_pron = pn.phones_for_word(word.text)

			if (len(word_pron) > 0):
				leading_sound = word_pron[0].split(" ")[0]

				if leading_sound not in alliteration_dict:
					alliteration_dict[leading_sound] = [word]
				else:
					alliteration_dict[leading_sound].append(word)

		return alliteration_dict

	"""
	Finds the alliteration within the tokenized list of words from spacy.
	"""
	def findAlliteration(self, tokenized_doc=None, logging=False):
		
		alliteration_dict = self.__findFirstSyllable(tokenized_doc) if (logging==False) else \
								self.__findFirstSyllableLogging(tokenized_doc)
								
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

		if (logging == True):
			for x in alliteration_list:
				print(x)
		
		return alliteration_list
	
	"""
	Finds all of the antonym pairs in the tokenized document
	"""	
	def findAntonymPairs(self, tokenized_doc):
		antonyms = set()
		
		# Loops through each word in tokenized document  
		for word in tokenized_doc:
			antonyms_word = self.dictionary.antonym(word.lemma_)
			
			# If there are antonyms for word
			if antonyms_word is not None:
				for other in tokenized_doc:
					if other.lemma_ in antonyms_word and (other, word) not in antonyms:
						antonyms.add((word, other))
						
		return antonyms
	