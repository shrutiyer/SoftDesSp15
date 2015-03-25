""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from collections import Counter

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	#Opens the file, reads all the lines and then chooses the start and end points
	lines = []
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line_a = 0
	curr_line_b = 0
	while lines[curr_line_a].find('THE ADVENTURES OF TOM SAWYER') == -1:
		curr_line_a += 1
	while lines[curr_line_b].find('End of the Project Gutenberg Ebook of Adventures of Tom Sawyer,')==-1:
		curr_line_b += 1
	#Creates a list of all the lines
	lines = lines[curr_line_a:curr_line_b]
	
	#Returns the list of words with no punctuation and lower case
	words = []
	for individual_line in lines:
		line_words = individual_line.split()
		for strings in line_words:
		 	word_to_add = strings.lower().strip(string.punctuation)
		 	words.append(word_to_add)
	return words


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	#Creates a tuple with most common words using Counter
	tupple = Counter(word_list).most_common(n)

	#Gets the first element of each tuple
	frequency = [it[0] for it in tupple]
	return frequency

print get_top_n_words(get_word_list('sawyer.txt'),20)