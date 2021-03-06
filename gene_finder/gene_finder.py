# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: siyer

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    # TODO: implement this
    if nucleotide == 'A':   #Finds the complementary
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    # TODO: implement this
    dna_reverse = dna [::-1] #Gets the reverse string
    dna_compl = ''
    for index in dna_reverse:
        newcleo = get_complement(index) #new complimentary nucleotide
        dna_compl = dna_compl + newcleo #Adds it to the empty string

    return dna_compl

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string. I modified the function 
        to return the rest of the string too.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTTATAA")
    ['ATGTTA', 'TAA']
    >>> rest_of_ORF("ATGTGGATGTATTGA")
    ['ATGTGGATGTAT', 'TGA']
    """
    # TODO: implement this
    dna_three = [dna[i:i+3] for i in range(0, len(dna), 3)] #Groups the string into a list of 3
    # list_name = [(x,y) for x in range(1,10) for y in range(1,10)]
    orf_sorted = dna_three  #Assignment just-in-case no stop codon are found
    orf_unsorted = ''
    for i in range(len(dna_three)):
        threes = dna_three[i]
        if threes == 'TAG' or threes == 'TAA' or threes == 'TGA':
            orf_sorted = dna_three[:i] #breaks into two strings, first is the ORF, second is rest of it
            orf_unsorted = dna_three[i:]
            break
        else:
            i = i+1
    orf_sorted = ''.join(orf_sorted)
    orf_unsorted = ''.join(orf_unsorted)
    return orf_sorted, orf_unsorted

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    # TODO: implement this
    dna_three = [dna[i:i+3] for i in range(0, len(dna), 3)]
    d = [] #output list of DNA strings
    while len(dna_three) > 1:
        threes = dna_three[0]
        if threes == 'ATG':
            orf_sorted_above = dna_three
            orf_sorted_update = ''.join(orf_sorted_above)
            d.append(rest_of_ORF(orf_sorted_update)[0])
            dna_three = rest_of_ORF(orf_sorted_update)[1]
            if len(dna_three) <= 1:
                break
            dna_three = [dna_three[i:i+3] for i in range(0, len(dna_three), 3)]
            threes = dna_three[0]
        elif len(dna_three) > 1 and threes != 'ATG':
            dna_three.pop(0)
    return d

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    # TODO: implement this
    dna_update = []
    dna_update.extend(find_all_ORFs_oneframe(dna))
    # dna_update += find_all_ORFs_oneframe(dna)
    dna_update += find_all_ORFs_oneframe(dna[1:])
    dna_update += find_all_ORFs_oneframe(dna[2:])
    return dna_update

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    # TODO: implement this
    dna_both = []
    dna_both += find_all_ORFs(dna)
    dna_compli = get_reverse_complement(dna)
    dna_both += find_all_ORFs(dna_compli)
    return dna_both

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    list_of_orfs = find_all_ORFs_both_strands(dna)
    if len(list_of_orfs) > 0: 
        return max(list_of_orfs, key = len)
    else:
        return ''

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    shuffle_list = []
    max_length_shuffled_orf = []
    max_individual_length_shuffled_orf = []

    for shuffle_num in range(num_trials + 1):
        s = shuffle_string(dna)
        shuffle_list.append(s)
        max_individual_length_shuffled_orf.append(longest_ORF(shuffle_list[shuffle_num]))
        max_length_shuffled_orf = max(max_individual_length_shuffled_orf, key = len)
    #print max_length_shuffled_orf
    return len(max_length_shuffled_orf)

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    dna_three = [dna[i:i+3] for i in range(0, len(dna), 3)]
    amino_acid = ''
    for k in range(0,len(dna_three)):
        threes = dna_three[k]
        if len(threes)==3:
            amino_acid_1 = aa_table[threes]
            amino_acid += amino_acid.join(amino_acid_1)
        k = k + 1
    return amino_acid

def gene_finder(dna):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.

        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    # TODO: implement this
    threshold = longest_ORF_noncoding(dna, 1500)

    both_strand_orfs_unthreshold = find_all_ORFs_both_strands(dna)
    both_strand_orfs_threshold = []

    for orfs in both_strand_orfs_unthreshold:
        if len(orfs) > threshold:
            both_strand_orfs_threshold.append(orfs)

    final_amino_conversion = map(coding_strand_to_AA, both_strand_orfs_threshold)
    return final_amino_conversion

dna = load_seq('./data/X73525.fa')
print gene_finder(dna)
