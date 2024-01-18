import time
import random
import os
import math

start = time.time()
start2 = time.clock()

#the location of file that you want to encrypt as a txt file instead of file
text = open(r"file")
text = text.read()


def caesar_encrypt(realText, step):
    outText = []
    cryptText = []

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

    for eachLetter in realText:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            crypting = (index + step) % 26
            cryptText.append(crypting)
            newLetter = uppercase[crypting]
            outText.append(newLetter)
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            crypting = (index + step) % 26
            cryptText.append(crypting)
            newLetter = lowercase[crypting]
            outText.append(newLetter)
    return outText

#for ceaser encryption
s = input("Enter the key: ")
result = ""
s = int(s)
result = caesar_encrypt(text, s)

dnadict = {
    "a": "ACAT",
    "b": "ACTG",
    "c": "ACCC",
    "d": "ACGA",
    "e": "TCAT",
    "f": "TCTG",
    "g": "TCCG",
    "h": "TCGT",
    "i": "CCAG",
    "j": "CCAT",
    "k": "CCCG",
    "l": "CCGG",
    "m": "GCAA",
    "n": "GCTT",
    "o": "GCCG",
    "p": "GCGC",
    "q": "ACTC",
    "r": "ACCG",
    "s": "TCTC",
    "t": "TCCC",
    "u": "CCTT",
    "v": "CCCC",
    "w": "GCTA",
    "x": "GCCC",
    "y": "AAAA",
    "z": "AATT",
    "A": "AACC",
    "B": "AAGG",
    "C": "TAAT",
    "D": "TATG",
    "E": "TACC",
    "F": "TAGA",
    "G": "CAAT",
    "H": "CATG",
    "I": "CACG",
    "J": "CAGT",
    "K": "GAAG",
    "L": "GATA",
    "M": "GACG",
    "N": "GAGG",
    "O": "AATA",
    "P": "AACG",
    "Q": "TATC",
    "R": "TACG",
    "S": "CATC",
    "T": "CACC",
    "U": "GATT",
    "V": "GACC",
    "W": "ATAA",
    "X": "ATTT",
    "Y": "ATCG",
    "Z": "ATGC",
    '0': "TTAA",
    '1': "TTTT",
    '2': "TTCC",
    '3': "TTGG",
    '4': "CTAT",
    '5': "CTTG",
    '6': "CTCC",
    '7': "CTGA",
    '8': "GTAT",
    '9': "GTTG",
    '<': "GTCG",
    '>': "GTGT",
    ',': "ATTA",
    '.': "ATCC",
    '?': "TTTA",
    '/': "TTCG",
    ':': "CTTC",
    ';': "CTCG",
    '"': "GTTC",
    '‘': "GTCC",
    '{': "AGAG",
    '[': "AGTA",
    '}': "AGGG",
    '|': "TGAA",
    '\'': "TGTT",
    '+': "TGCG",
    '=': "TGGC",
    '_': "CGAA",
    '-': "CGTT",
    '(': "CGGG",
    ')': "CGCC",
    '*': "GGAT",
    '&': "GGTG",
    '^': "GGCC",
    '%': "GGGA",
    '$': "AGTT",
    '#': "AGCC",
    '@': "TGTA",
    '!': "TGCC",
    '~': "CGTA",
    '`': "CGCG",
    '€': "GGTC",
    '£': "GGCG",
    " ": "ACGT",
    '\n': "TTTG",
    '’': "AAAG",
    '“': "CCCA",
    '”': "TCGC",
    '–': "CGAT",
    ']': "TAGC"
}

encode = []
lr = len(result)
i = 0
while i < lr:
    encode.append(dnadict[result[i]])
    i = i + 1

encode = ''.join(encode)
# print(encode)
binaryencode = []
lencode = len(encode)
j = 0
while j < lencode:
    if encode[j] == 'A':
        binaryencode.append('00')
    elif encode[j] == 'C':
        binaryencode.append('01')
    elif encode[j] == 'G':
        binaryencode.append('10')
    elif encode[j] == 'T':
        binaryencode.append('11')
    j += 1

binaryencode = ''.join(binaryencode)
# print(binaryencode)
complimentbinary = []
lbinaryencode = len(binaryencode)
t = 0

while t < lbinaryencode:
    if binaryencode[t] == '1':
        complimentbinary.append('0')
    elif binaryencode[t] == '0':
        complimentbinary.append('1')
    t = t + 1

complimentbinary = ''.join(complimentbinary)
# print(complimentbinary)
split_strings = []

n = 8

for index in range(0, len(complimentbinary), n):
    split_strings.append(complimentbinary[index:index + n])

lcomplimentbinary = len(split_strings)
z = 0
copylist = split_strings.copy()
complimentbinary2 = []
t = 0
while z < lcomplimentbinary:
    x = 0
    lbyte_list = len(split_strings[z])
    while x < lbyte_list:
        if x == 0:
            complimentbinary2.insert(t, copylist[z][x])
        elif x == 1:
            complimentbinary2.insert(t, copylist[z][x + 2])
        elif x == 2:
            complimentbinary2.insert(t, copylist[z][x + 3])
        elif x == 3:
            complimentbinary2.insert(t, copylist[z][x - 2])
        elif x == 4:
            complimentbinary2.insert(t, copylist[z][x + 2])
        elif x == 5:
            complimentbinary2.insert(t, copylist[z][x - 3])
        elif x == 6:
            complimentbinary2.insert(t, copylist[z][x - 2])
        elif x == 7:
            complimentbinary2.insert(t, copylist[z][x])
        x += 1
        t += 1
    z += 1

complimentbinary2 = ''.join(complimentbinary2)
# print(complimentbinary2)
split_strings_DNA = []

ndna = 2

for indexdna in range(0, len(complimentbinary2), ndna):
    split_strings_DNA.append(complimentbinary2[indexdna:indexdna + ndna])

DNAstream = []
lensdna = len(split_strings_DNA)
p = 0
while p < lensdna:
    if split_strings_DNA[p] == '00':
        DNAstream.append('A')
    elif split_strings_DNA[p] == '01':
        DNAstream.append('C')
    elif split_strings_DNA[p] == '10':
        DNAstream.append('G')
    elif split_strings_DNA[p] == '11':
        DNAstream.append('T')
    p += 1
DNAstreamc = DNAstream.copy()
DNAstreamc = ''.join(DNAstreamc)
# print(DNAstreamc)

mrna = [sub.replace('T', 'U') for sub in DNAstream]
mrna2 = mrna.copy()
mrna2 = ''.join(mrna2)
# print(mrna2)
lmrna = len(mrna)
trna = []
q = 0
while q < lmrna:
    if mrna[q] == 'A':
        trna.append('U')
    elif mrna[q] == 'U':
        trna.append('A')
    elif mrna[q] == 'G':
        trna.append('C')
    elif mrna[q] == 'C':
        trna.append('G')
    q += 1
trna2 = trna.copy()
trna2 = ''.join(trna2)
# print(trna2)

DNAstream2 = [sub.replace('U', 'T') for sub in trna]

DNAstream2 = ''.join(DNAstream2)
# print(DNAstream2)
#write location for the file instead of file
path = r'file'
# f = open(os.path.join(path,"myfile.txt"), "x")
f = open(os.path.join(path, "myfile.txt"), "w")
f.write(DNAstream2)
f.close()

end = time.time()
end2 = time.clock()

print(f"Runtime of the program is {end - start}")
print(f"Runtime of the program is {end2 - start2}")
