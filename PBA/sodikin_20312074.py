# -*- coding: utf-8 -*-
"""SODIKIN_20312074.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15UW3OXXlerF6bYaTZTKBl1Y1sRCfSQHQ
"""

#Import Package
import math

#Definisi Fungsi Cosine Similarity
def vektorisasi(vec1, vec2, vec3):
    vec1 = list(vec1)
    vec2 = list(vec2)
    vec3 = list(vec3)
    hasil = 0
    for i, v in enumerate(vec1):
        hasil += v * vec2[i] * vec3[i]
    mag_1 = math.sqrt(sum([x**2 for x in vec1]))
    mag_2 = math.sqrt(sum([x**2 for x in vec2]))
    mag_3 = math.sqrt(sum([x**2 for x in vec3]))
    return hasil / (mag_1 * mag_2 * mag_3)

#2 Kalimat yang ingin dihitung cosine similaritynya 
kalimat1 = 'ikan ikan suka makan nasi'
kalimat2 = 'ikan kucing makan makan'
kalimat3 = 'kucing makan nasi nasi'

#Pembentukan Vektor Bag Of Word
cosineBoW=[]
BoWA = kalimat1.split(' ')
BoWB = kalimat2.split(' ')
BoWC = kalimat3.split(' ')

uniqueWords = set(BoWA).union(set(BoWB).union(set(BoWC)))
numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in BoWA:
    numOfWordsA[word] += 1
numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in BoWB:
    numOfWordsB[word] += 1
numOfWordsC = dict.fromkeys(uniqueWords, 0)
for word in BoWC:
    numOfWordsC[word] += 1
#Perhitungan Cosine Similarity
hasil = vektorisasi(numOfWordsA.values(),numOfWordsB.values(),numOfWordsC.values())
print('nilai :', hasil)

"""ketika melakukan vektorisasi teks dengan menggunakan Bag Of Word (BoW), maka nilai cosine similarity akan selalu bernilai non-negatif 
karena elemen-elemen dalam vektor adalah banyaknya suatu kata bernilai non-negatif.
Akibatnya, Cosine Similarity dengan BoW terbatas untuk mendeteksi kemiripan suatu teks dari segi permukaan atau leksikal saja. Ia belum bisa mendeteksi apakah 2 kalimat itu memiliki informasi yang berlawanan.

"""

#Import Package  menggunakan numpy
import numpy as np

#definisi array dari masing-masing kalimat
kalimat1array= np.array(list(numOfWordsA.values()))
kalimat2array= np.array(list(numOfWordsB.values()))
kalimat3array= np.array(list(numOfWordsC.values()))

#euclidean distance
d = np.linalg.norm(kalimat1array - kalimat2array - kalimat3array)
d

"""euclidean distance tidak seperti cosine similarity yang berada pada batas tertentu. 
Sehingga untuk menentukan apakah jaraknya sudah cukup dekat apa belum sebaiknya digunakan vektor-vektor lain sebagai pembanding atau bisa dilakukan penentuan batas/threshold sendiri oleh pembuat model.
"""