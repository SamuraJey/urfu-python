import pandas as pd
import math


class Document:
    def __init__(self, text):
        # Конструктор класса. Принимает на вход текст документа.
        # задаёт его в качестве атрибута класса и разбивает на слова.
        self.text = text
        self.word_dict = {}
        self.list_of_words = self.text.split()
        self.tf = {}
        self.tfidf = {}

    def compute_word_dict(self, word_set):
        # Считает количество вхождений каждого слова в документe.
        # Создаём словарь, где ключи - слова из множества слов, а значения - 0.
        self.word_dict = dict.fromkeys(word_set, 0)
        for word in self.list_of_words:
            # Когда встречаем слово, увеличиваем его значение на 1.
            self.word_dict[word] += 1

    def compute_tf(self):
        # Считает частоту встречаемости каждого слова в документе.
        for word, count in self.word_dict.items():
            # Делим количество вхождений слова на общее количество слов в документе.
            self.tf[word] = count / len(self.list_of_words)
        return self.tf

    def compute_tfidf(self, idfs):
        # Считает tf-idf для каждого слова в документе.
        # idfs - словарь, где ключи - слова, а значения - idf для каждого слова
        # его получаем из Corpus'а.
        for word, tf in self.tf.items():
            self.tfidf[word] = round(tf * idfs[word], 3)


class Corpus:
    def __init__(self, documents):
        # Конструктор класса. Принимает на вход список документов.
        self.documents = documents
        self.word_set = set()
        self.idfs = {}

    def compute_word_set(self):
        # Считает множество слов, встречающихся во всех документах.
        for doc in self.documents:
            self.word_set = self.word_set.union(set(doc.list_of_words))

    def get_word_set_len(self):
        # Возвращает количество уникальных слов во всех документах.
        return len(self.word_set)

    def compute_idfs(self):
        # Считает idf для каждого слова
        num_documents = len(self.documents)
        for word in self.word_set:
            # Считаем количество документов, в которых встречается слово.
            # Возможно, это не очень эффективно.
            freq = sum(
                [1 for doc in self.documents if word in doc.list_of_words])
            self.idfs[word] = math.log10(num_documents / float(freq))

    def compute_tfidf(self):
        # Считает tf-idf для каждого слова в каждом документе.
        for doc in self.documents:
            doc.compute_tfidf(self.idfs)

    def get_tfidf_dataframe(self):
        # Возвращает таблицу с tf-idf. Форматирование от pandas
        rows = [doc.tfidf for doc in self.documents]
        return pd.DataFrame(rows)


def main():
    file1 = 'Second Lection/1.txt'
    file2 = 'Second Lection/2.txt'
    file3 = 'Second Lection/3.txt'
    file4 = 'Second Lection/4.txt'

    # with open(file1, errors='ignore') as f:
    #     doc_a = Document(f.read().casefold())

    # with open(file2, errors='ignore') as f:
    #     doc_b = Document(f.read().casefold())

    # with open(file3, errors='ignore') as f:
    #     doc_c = Document(f.read().casefold())

    # with open(file4, errors='ignore') as f:
    #     doc_d = Document(f.read().casefold())

    # corpus = Corpus([doc_a, doc_b, doc_c, doc_d, ])

    documents = []
    try:
        for file in [file1, file2, file3, file4]:
            with open(file, errors='ignore') as f:
                documents.append(Document(f.read().casefold()))
    except MemoryError:
        raise NotImplementedError
    except OSError:
        print("Ошибка чтения файла")
        return

    corpus = Corpus(documents)

    corpus.compute_word_set()
    for doc in corpus.documents:
        doc.compute_word_dict(corpus.word_set)
        doc.compute_tf()

    corpus.compute_idfs()
    corpus.compute_tfidf()

    print(corpus.get_word_set_len())
    print(corpus.get_tfidf_dataframe())


if __name__ == '__main__':
    main()
