#Import Package
import math

#Definisi Fungsi Cosine Similarity
def cosine_sim(vec1, vec2):
    vec1 = list(vec1)
    vec2 = list(vec2)
    dot_prod = 0
    for i, v in enumerate(vec1):
        dot_prod += v * vec2[i]
    mag_1 = math.sqrt(sum([x**2 for x in vec1]))
    mag_2 = math.sqrt(sum([x**2 for x in vec2]))
    return dot_prod / (mag_1 * mag_2)

#2 Kalimat yang ingin dihitung cosine similaritynya 
kalimat1 = 'classification produce discrete value'
kalimat2 = 'discrete value on classification'

#Pembentukan Vektor Bag Of Word
cosineBoW=[]
bagOfWordsA = kalimat1.split(' ')
bagOfWordsB = kalimat2.split(' ')
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))
numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1
numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1
    
#Perhitungan Cosine Similarity
cosine_sim(numOfWordsA.values(),numOfWordsB.values())