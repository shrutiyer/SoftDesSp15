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
    if nucleotide == 'A':
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
    dna_reverse = dna [::-1]
    dna_compl = ''
    for index in dna_reverse:
        newcleo = get_complement(index)
        dna_compl = dna_compl + newcleo

    return dna_compl

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTTATAA")
    'ATGTTA'
    >>> rest_of_ORF("ATGTGGATGTATTGA")
    'ATGTGGATGTAT'
    """
    # TODO: implement this
    dna_three = [dna[i:i+3] for i in range(0, len(dna), 3)]
    orf_sorted = dna_three
    orf_unsorted = ''
    for i in range(len(dna_three)):
        threes = dna_three[i]
        if threes == 'TAG' or threes == 'TAA' or threes == 'TGA':
            orf_sorted = dna_three[:i]
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
    >>> find_all_ORFs_oneframe("ATGTGAATGTAAATGTAG")
    ['ATG', 'ATG', 'ATG']
    """
    # TODO: implement this
    dna_three = [dna[i:i+3] for i in range(0, len(dna), 3)]
    d = []
    i = 0
    while len(dna_three) > 1:
        threes = dna_three[i]
        if threes == 'ATG':
            orf_sorted_above = dna_three[i:]
            orf_sorted_update = ''.join(orf_sorted_above)
            d.append(rest_of_ORF(orf_sorted_update)[0])
            dna_three = rest_of_ORF(orf_sorted_update)[1]
            if len(dna_three) <= 1:
                print 'yay'
                break
            dna_three = [dna_three[i:i+3] for i in range(0, len(dna_three), 3)]
            i = 0
            threes = dna_three[i]
        elif len(dna_three) > 1 and threes != 'ATG':
            i = i+1
        else:
            break
    print d

find_all_ORFs_oneframe("TAGATGCTAGCGCATCGA")