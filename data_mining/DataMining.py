"""@author: siyer
This code runs and graphs the cosine similary for three books
reference1 = Jane Eyre written by Charlotte Bronte
reference2 = Oliver Twist written by Charles Dickens
sample1 = Villette written by Charlotte Bronte
The program treats Villette as an unknown text and checks for stylometry
"""

import re, math
from collections import Counter
from random import randint
import matplotlib.pyplot as plt

def cosine_similarity(vec1d, vec2d):
     """
            Computes the cosine similarity of two texts
            vec1d and vec2d: Tuple of frequently used words from text 1 and 2
     """
     vec1 = dict(vec1d) #Converts vec1d and vec2d to a dictionary as tuples are immutable
     vec2 = dict(vec2d)

     vec1a = remove_common(vec1) #Removes the most commonly used words
     vec2a = remove_common(vec2)

     common = set(vec1a.keys()) & set(vec2a.keys()) #Finds the common keys in both the dictionaries
     top = sum([vec1a[x] * vec2a[x] for x in common]) #Numerator of the cosine function

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     bottom = math.sqrt(sum1) * math.sqrt(sum2) #Denominator of the cosine function

     return float(top)/bottom

def text_to_vector(text,n):
     """
     Takes in a .txt file and n to output the n most common 
     words used  
     """
     words = re.findall(r'\w+', open(text).read().lower()) #Opens and reads the .txt file
     tupple = Counter(words).most_common(n) #Creates a tuple of the word and the frequency
     return tupple

def remove_common(dictionar):
    """
    Removes commomly used words and returns in form of dictionary
    """
    del dictionar['the'] #Deletes the key in the dict
    del dictionar['a']
    del dictionar['and']
    return dictionar

def compare_cosine():
    """
    This is the main function which compares all the three texts and 
    gives output of the cosine similarity.
    It also checks how the cosine similarity changes as the value of 
    n increases.
    """
    Y1 = []
    Y2 = []
    X = []
    for n in range(60,1000,20):
        reference1 = text_to_vector('JaneEyre.txt',n)
        reference2 = text_to_vector('Oliver.txt',n)
        sample1 = text_to_vector('Villette.txt',n)
        cos1 = cosine_similarity(sample1, reference1)
        cos2 = cosine_similarity(sample1, reference2)
        Y1.append(round(cos1,3)) #Rounds off the numbers
        Y2.append(round(cos2,3))
        X.append(n)
    return X,Y1,Y2

[X,Y1,Y2] = compare_cosine()
plt.plot(X, Y1,'ro',X, Y2,'b^') #PLots the two cosine value lists

plt.title('Text similarity of an unknown book with two reference books')
plt.xlabel('Number of words used')
plt.ylabel('Cosine Similarity Values')
plt.show()
