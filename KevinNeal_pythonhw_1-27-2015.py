#Kevin Neal, EEB 234
#homework: Python for Biologists examples on pp 38-40, due 1-27-2015

from __future__ import division

#calculating AT content:
#ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

Acount = my_dna.count("A")
Tcount = my_dna.count("T")

#print the AT content of this sequence: (A+T)/length
ATcontent = (Acount+Tcount)/len(my_dna)
print(ATcontent)

#printing complement of a sequence:

#my_dna_complement = my_dna.replace("ACGT","TGCA") #doesn't work, searches exact string. hmm...

Atot = my_dna.replace("A","t")
Ttoa = Atot.replace("T","a")
Ctog = Ttoa.replace("C","g")
Gtoc = Ctog.replace("G","c")
my_dna_complement = Gtoc.upper()
print(my_dna_complement)

#calculate size of two fragments after EcoRI cut at G*AATTC
my_dna2 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
firstfraglength = my_dna2.find(GAATTC) + 1 #should equal 22
#will print position of start of this sequence; to return length of first fragment, 
#add 1 to the position to tell the number of characters before the cut site, *
#and print the length of the full sequence less the length of this first fragment

secondfraglength = len(my_dna2) - firstfraglength #should equal 33

print("Fragment 1 is " + str(firstfraglength) + " bp")
print("Fragment 2 is " + str(secondfraglength) + " bp")

#splicing out introns
my_dna3 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
print(len(my_dna3)) #123
print(my_dna3[0:63] + my_dna3[90:123] #prints exons between first and 63rd characters, and 91st to 123rd (last)

#calculate percentage of sequence that is coding (exonic)
exonlength = len(my_dna3[0:63]) + len(my_dna3[90:123])
exonpercent = exonlength / len(my_dna3)

#print out my_dna3 with exons in uppercase and intron in lowercase
exon1 = my_dna3[0:63]
exon2 = my_dna3[90:123]
intron = my_dna3[63:90]
print(exon1 + intron.lower() + exon2)