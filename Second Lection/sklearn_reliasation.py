from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

file1 = 'Second Lection/1.txt'
file2 = 'Second Lection/2.txt'
file3 = 'Second Lection/3.txt'
file4 = 'Second Lection/4.txt'

with open(file1, errors='ignore') as f:
    doc_a = f.read().lower()

with open(file2, errors='ignore') as f:
    doc_b = f.read().lower()

with open(file3, errors='ignore') as f:
    doc_c = f.read().lower()

with open(file4, errors='ignore') as f:
    doc_d = f.read().lower()

documents = [doc_a, doc_b, doc_c, doc_d]
vect = TfidfVectorizer()
tfidf_matrix = vect.fit_transform(documents)
df = pd.DataFrame(tfidf_matrix.toarray(), columns=vect.get_feature_names_out())
print(df)
