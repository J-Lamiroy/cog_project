"""
The purpose of this file is to generate a worldcloud from a plaintext file.
As of now, two extra operations are planned:
	- Removing words from a separate list from the wordcloud, this will be
	  typically used for common English words, but allows supports for other
	  languages

	- Finding and removing proper names, which could give too much context
	  through popular knowledge (eg: Sherlock Holmes mostly appears in novels)

Source texts will have a category attached, which will be passed on to the word
cloud.
"""

def file_to_list(file_name):
	"""
	This function takes a file name as an input, and turns its lines into a list
	Its main use is being used in wordcloud
	"""
	l = []
	f = open(file_name)
	line = f.readline()

	while line != "":
		l.append(line[:-1]) #the trailing \n is chopped off
		line = f.readline()

	f.close()
	return l

def prepare(word):
	"""
	chops off unwanted extra characters, like punctuation. It's recursive
	"""

	if word[-1] in ['.', ',', ';', ':', '?', '!', '\n', '\t']:
		return prepare(word[:-1])

	else:
		return word.upper()


def wordcloud(source_name, out_name, cull_list, n_words):
	"""
	This is utils.py's main function, taking a source file and turning it into
	a Bag of Words representation. It handles selectively removing words from
	cull_list, and proper names (not actually implemented yet)
	"""
	source = open(file_name, "r")
	out = open(out_name, "w")

	first_line = source.readline()
	out.write(first_line)
	#copies the first line of the source file, that contains data such as type
	
	tally = {}

	line = source.readline()

	while line != '': #just using .read and then splitting along \n and spaces would be a bit more tedious
		words = [prepare(w) for w in line.split()]
		words = filter(lambda w: w not in cull_list, words)
		#these two lines take the list of words, cleans them from punctuation
		#and removes commonly used words

		#DO PROPER NOUNS

		for w in words:
			if w not in tally:
				tally[w] = 0
			tally[w] += 1
		#adds words to the tally

		line = source.readline()

	word_list = [(-tally[w], w) for w in tally]
	#words and their associated count, to be sorted. The negative and order
	#of the weight and word is to make the next line easy:
	word_list.sort()

	for i in range(n_words):
		out.write(word_list[i])

	source.close()
	out.close()