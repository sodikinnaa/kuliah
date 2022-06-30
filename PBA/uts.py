#Import Package
import math

#Definisi Fungsi Cosine Similarity
def cosine_sim(vec1, vec2, vec3):
    vec1 = list(vec1)
    vec2 = list(vec2)
    vec3 = list(vec3)
    dot_prod = 0
    for i, v in enumerate(vec1):
        dot_prod += v * vec2[i] * vec3[i]
    mag_1 = math.sqrt(sum([x**2 for x in vec1]))
    mag_2 = math.sqrt(sum([x**2 for x in vec2]))
    mag_3 = math.sqrt(sum([x**2 for x in vec3]))
    return dot_prod / (mag_1 * mag_2 * mag_3)

#2 Kalimat yang ingin dihitung cosine similaritynya 
kalimat1 = 'ikan ikan suka makan nasi'
kalimat2 = 'ikan kucing makan makan'
kalimat3 = 'kucing makan nasi nasi'

#Pembentukan Vektor Bag Of Word
cosineBoW=[]
bagOfWordsA = kalimat1.split(' ')
bagOfWordsB = kalimat2.split(' ')
bagOfWordsC = kalimat3.split(' ')

uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB).union.(bagOfWordsC))
numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1
numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1
numOfWordsC = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsC:
    numOfWordsC[word] += 1
#Perhitungan Cosine Similarity
cosine_sim(numOfWordsA.values(),numOfWordsB.values(),numOfWordsC.values())