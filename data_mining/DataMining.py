"""@author: siyer
This code runs and graphs the cosine similary for three books
reference1 = Jane Eyre written by Charlotte Bronte
reference2 = Oliver Twist written by Charles Dickens
sample1 = Villette written by Charlotte Bronte
The program treats Villette as an unknown text and checks for stylometry
"""

"""
Reading your reflection, I'm super happy to see you really developing as a programmer. Reading documentation
and using libraries is a very big part of programming and I'm really glad to see you realize that.

I'm also super happy to see the way you set up your model. Coding is only a tiny part of the story, most of
the improtant work is structuring and modeling your project. You seem to be focusing on that, which I'm really
glad to see.

I'm also glad to hear about your reflection on iterative development. Geez, I dont even need to be your ninja,
you're having a ton of great insights programmers may only realize way later on. Coding is a lot more than the
typing on a computer, it's about modeling, iterating, and using libraries. Great!

As per your code, good job splitting functions and using libraries. Only thing missing: testing. 

Also, you have a lot of chunks of repetitive code with vec1, vec2, sum1, sum2, etc. See if you can make that more elegant.
Repetitiveness isn't so great in code, and you can always find a more elegant way to shrink that down. If you have
more questions on how, feel free to meet with me in person.

+Functionality: 5/5
+Documentation: 4.5/5 (Test code)
+Style: 4.5/5 (Repetitiveness)
+CheckIn: yes
+Total: 4.75/5

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
