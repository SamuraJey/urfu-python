import pandas as pd
import math

class Document:
    def __init__(self, text):

        self.text = text
        self.word_dict = {}
        self.list_of_words = self.text.split()
        self.tf = {}
        self.tfidf = {}

    def compute_word_dict(self, word_set):
        self.word_dict = dict.fromkeys(word_set, 0)
        for word in self.list_of_words:
            self.word_dict[word] += 1

    def compute_tf(self):
        for word, count in self.word_dict.items():
            self.tf[word] = count / len(self.list_of_words)
        return self.tf

    def compute_tfidf(self, idfs):
        for word, tf in self.tf.items():
            self.tfidf[word] = round(tf * idfs[word], 3)


class Corpus:
    def __init__(self, documents):
        self.documents = documents
        self.word_set = set()
        self.idfs = {}

    def compute_word_set(self):
        for doc in self.documents:
            self.word_set = self.word_set.union(set(doc.list_of_words))

    def compute_idfs(self):
        num_documents = len(self.documents)
        for word in self.word_set:
            freq = sum([1 for doc in self.documents if word in doc.list_of_words])
            self.idfs[word] = math.log10(num_documents / float(freq))

    def compute_tfidf(self):
        for doc in self.documents:
            doc.compute_tfidf(self.idfs)

    def get_tfidf_dataframe(self):
        rows = []
        for doc in self.documents:
            rows.append(doc.tfidf)
        return pd.DataFrame(rows)

def main():
    file1 = 'Second Lection/1.txt'
    file2 = 'Second Lection/2.txt'
    file3 = 'Second Lection/3.txt'
    file4 = 'Second Lection/4.txt'

    with open(file1, errors='ignore') as f:
        doc_a = Document(f.read().lower())

    with open(file2, errors='ignore') as f:
        doc_b = Document(f.read().lower())

    with open(file3, errors='ignore') as f:
        doc_c = Document(f.read().lower())
    
    with open(file4, errors='ignore') as f:
        doc_d = Document(f.read().lower())


    corpus = Corpus([doc_a, doc_b, doc_c, doc_d, ])

    corpus.compute_word_set()
    for doc in corpus.documents:
        doc.compute_word_dict(corpus.word_set)
        doc.compute_tf()

    corpus.compute_idfs()
    corpus.compute_tfidf()
    print(doc_a.compute_tf())
    print(corpus.get_tfidf_dataframe())

if __name__ == '__main__':
    main()