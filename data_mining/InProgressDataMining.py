"""@author: siyer
This code runs and plots a heatmap the cosine similary for four books
reference1 = Jane Eyre written by Charlotte Bronte
reference2 = Oliver Twist written by Charles Dickens
reference3 = Villette written by Charlotte Bronte
reference4 = Wuthering Heights by Emily Bronte

This code is a work in progress.
Problems encountered in testing the code: Unable to download books off 
Project Gutenberg (403 Error).
So, the outputs is a heatmap with just 4 books.
My intention was to arrange the books, published over a century,
chronologically and check for change in writing styles over the century.

The output of the function is a heatmap
"""
import re, math
from collections import Counter
import glob
from pylab import *
import numpy as np
import decimal
from matplotlib import pyplot as plt

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

flist_unsorted = glob.glob("*.txt") #A list of all .txt files in the current folder
flist = sorted(flist_unsorted) #Sorts the files in chronological order
print flist #Printing just to check the order
samples = []
n = 10
for i in range(0,len(flist)):
    temp_sample = text_to_vector(flist[i],n) #Creates a tuple of the sample
    samples.append(temp_sample)

for_plotting = []
for xa in range(0,len(flist)):
     new_row_list = []
     for ya in range(0,len(flist)):
          t = cosine_similarity(samples[xa],samples[ya])
          point = [flist[xa], flist[ya], round(t,3)]
          new_row_list.append(round(t,3))
     for_plotting.append(new_row_list)

def plot():
     """
     Plots the heatmap
     """
     d = np.array(for_plotting)
     print d
     column_labels = flist #X and y labels are the same
     row_labels = flist

     fig, ax = plt.subplots()
     heatmap = ax.pcolor(d, cmap=plt.cm.Blues)

     ax.set_xticks(np.arange(d.shape[0])+0.5, minor=False) #centers the labels
     ax.set_yticks(np.arange(d.shape[1])+0.5, minor=False)
     
     ax.set_xticklabels(row_labels, minor=False)
     ax.set_yticklabels(column_labels, minor=False)
     
     plt.show()

plot()