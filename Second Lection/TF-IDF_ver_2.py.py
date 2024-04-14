import math
import pandas as pd

file1 = 'Second Lection/1.txt'
file2 = 'Second Lection/2.txt'

with open(file1, errors='ignore') as f:
    doc_a = f.read().lower()

with open(file2, errors='ignore') as f:
    doc_b = f.read().lower()


def compute_tf(word_dict, bow):
    tf_dict = {}
    bow_count = len(bow)
    for word, count in word_dict.items():
        tf_dict[word] = count / float(bow_count)
    return tf_dict


def compute_idf(doc_list):
    idf_dict = {}
    N = len(doc_list)

    idf_dict = dict.fromkeys(doc_list[0].keys(), 0)
    for doc in doc_list:
        for word, val in doc.items():
            if val > 0:
                idf_dict[word] += 1

    for word, val in idf_dict.items():
        idf_dict[word] = math.log(N / float(val))

    return idf_dict


def compute_tfidf(tf_bow, idfs):
    tfidf = {}
    for word, val in tf_bow.items():
        tfidf[word] = val * idfs[word]
    return tfidf


bow_a = doc_a.split()
bow_b = doc_b.split()

word_set = set(bow_a).union(set(bow_b))

word_dict_a = dict.fromkeys(word_set, 0)
word_dict_b = dict.fromkeys(word_set, 0)


for word in bow_a:
    word_dict_a[word] += 1

for word in bow_b:
    word_dict_b[word] += 1

tf_a = compute_tf(word_dict_a, bow_a)
tf_b = compute_tf(word_dict_b, bow_b)
print(tf_a)
print(tf_b)

idfs = compute_idf([word_dict_a, word_dict_b])
print(idfs)

tfidf_a = compute_tfidf(tf_a, idfs)
tfidf_b = compute_tfidf(tf_b, idfs)

res = pd.DataFrame([tfidf_a, tfidf_b])
print(res)
