import math
import re

with open('Second Lection/1.txt', encoding='utf-8', errors='ignore') as f:
    doc_a = f.read()

with open('Second Lection/2.txt', encoding='utf-8', errors='ignore') as f:
    doc_b = f.read()


doc_a = 'this document is first document'
doc_b = 'this document is the second document'


# Now create a dictionary of words and their occurence for each document in the corpus (collection of documents).


def extract_words(text):
    # Используем регулярное выражение для удаления символов, не являющихся буквами
    # и разделяем строку на слова
    words = re.findall(r'\b\w+\b', text.lower())
    return words


def create_word_dict(document):

    words1 = set(extract_words(document))
    lenght_of_words1 = len(words1)

    dict_first = dict.fromkeys(words1, 0)

    for word in words1:
        dict_first[word] += 1

    return dict_first, lenght_of_words1


def compute_term_frequency(document):

    dict_first,  lenght_of_words1 = create_word_dict(document)
    term_frequency_dictionary = {}

    for word, count in dict_first.items():
        term_frequency_dictionary[word] = count / float(lenght_of_words1)

    return term_frequency_dictionary


def compute_inverse_document_frequency(full_doc_list):
    idf_dict = {}
    length_of_doc_list = len(full_doc_list)

    idf_dict = dict.fromkeys(full_doc_list[0].keys(), 0)
    for word, value in idf_dict.items():
        idf_dict[word] = math.log(length_of_doc_list / (float(value) + 1))

    return idf_dict


print(compute_term_frequency(doc_a))
print(compute_term_frequency(doc_b))
kek = [compute_term_frequency(doc_a), compute_term_frequency(doc_b)]
print(kek)
print(compute_inverse_document_frequency(kek))
