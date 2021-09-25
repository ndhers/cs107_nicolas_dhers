def dna_complement(dna: str):
	if not dna:
		return None
	dna = dna.upper()

	bases = ['A','T','G','C']
	complement = ''
	for i in dna:
		if i not in bases:
			return None
		if i == 'A':
			complement += 'T'
		if i == 'T':
			complement += 'A'
		if i == 'G':
			complement += 'C'
		if i == 'C':
			complement += 'G'

	return complement

print('Example input string: '+'AaTggC \n')
complement = dna_complement('AaTggC')
print('Corresponding complement: '+complement+'\n')
print('Example of wrong input string: '+'2dTGpC \n')
complement = dna_complement('2dTGpC')
print('Corresponding complement: '+str(complement)+'\n')
