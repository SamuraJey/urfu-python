import re
import math

def count_unique_words(file1, file2):
    # Считаем количество уникальных слов в каждом файле
    words1 = set()
    with open(file1, encoding='utf-8', errors='ignore') as f:
        for line in f:
            words1 |= set(re.findall(r'\w+', line))
    
    words2 = set()
    with open(file2, encoding='utf-8', errors='ignore') as f:
        for line in f:
            words2 |= set(re.findall(r'\w+', line))
    
    return len(words1), len(words2)

def calculate_tf(file1, file2):
    # Считаем tf-idf для каждого слова в каждом файле
    tf1 = {}
    with open(file1, encoding='utf-8', errors='ignore') as f:
        for line in f:
            for word in re.findall(r'\w+', line):
                if word not in tf1:
                    tf1[word] = 0
                tf1[word] += 1
    
    tf2 = {}
    with open(file2, encoding='utf-8', errors='ignore') as f:
        for line in f:
            for word in re.findall(r'\w+', line):
                if word not in tf2:
                    tf2[word] = 0
                tf2[word] += 1
    
    # Определяем tf для каждого слова
    tf_final = {}
    for word in tf1:
        tf_final[word] = tf1[word] / len(tf1)
    for word in tf2:
        tf_final[word] = tf2[word] / len(tf2)

    
    
    return tf_final

# Пример использования
file1 = 'Second Lection/1.txt'
file2 = 'Second Lection/2.txt'

num_unique_words1, num_unique_words2 = count_unique_words(file1, file2)
print(f'Количество уникальных слов в {file1}: {num_unique_words1}')
print(f'Количество уникальных слов в {file2}: {num_unique_words2}')

tfidf = calculate_tf(file1, file2)
for word in tfidf:
    print(f'{word}: {tfidf[word]}')