def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
	''' (str) -> Boolean
	Return True if and only if the DNA sequence is valid
	(that is, it contains no characters other than 'A', 'T', 'C' and 'G')

	>>> is_valid_sequence('ATCGGC')
	True
	>>> is_valid_sequence('ATCBGGC')
	False
	'''
	bads = 0
	
	for char in dna:
		if char not in 'ATCG':
			bads = bads + 1
	return not bads > 0

def insert_sequence(dna1, dna2, index):
	''' (str, str, int) -> str
	Return the DNA sequence obtained by inserting the second DNA sequence
	into the first DNA sequence at the given index.

	Precondition: assume that the index is valid.
	>>> insert_sequence('CCGG', 'AT', 2)
	CCATGG
	>>> insert_sequence('CC', 'AT', 2)
	CCAT
	'''
	
	return dna1[0:index] + dna2 + dna1[index: ]

def get_complement(nucleotide):
    ''' (str) ->str
    Return the nucleotide's complement. A and T can be bonded together,
    and thus complement each other; similarly, C and G are
    complements of each other.
    >>> insert_sequence('A')
    'T'
    >>> insert_sequence('C')
    'G'
    '''

    sequence = ''
    for char in nucleotide:
        if char == 'A':
            sequence = sequence + 'T'
        if char == 'T':
            sequence = sequence + 'A'
        if char == 'G':
            sequence = sequence + 'C'
        if char == 'C':
            sequence = sequence + 'G'

    return sequence

def get_complementary_sequence(sequence):
    ''' (str) ->str
    Return the nucleotide's complement. A and T can be bonded together,
    and thus complement each other; similarly, C and G are
    complements of each other.
    >>> insert_sequence('A')
    'T'
    >>> insert_sequence('C')
    'G'
    '''

    seq = ''
    for char in sequence:
        if char == 'A':
            seq = seq + 'T'
        if char == 'T':
            seq = seq + 'A'
        if char == 'G':
            seq = seq + 'C'
        if char == 'C':
            seq = seq + 'G'

    return seq
