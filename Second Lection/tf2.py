import math

def calculate_tf(word, document):
    total_words = len(document.split())
    word_frequency = document.split().count(word)
    tf = word_frequency / total_words
    return tf

def calculate_idf(word, documents):
    total_documents = len(documents)
    documents_with_word = sum(1 for doc in documents if word in doc)
    idf = math.log(total_documents / (1 + documents_with_word))
    return idf

def calculate_tfidf(documents):
    unique_words = set()
    for doc in documents:
        unique_words.update(doc.split())

    tfidf_scores = {}
    for word in unique_words:
        tfidf_scores[word] = []
        for doc in documents:
            tf = calculate_tf(word, doc)
            idf = calculate_idf(word, documents)
            tfidf = tf * idf
            tfidf_scores[word].append(tfidf)

    return tfidf_scores

# Example usage
document1 = "John likes apple"
document2 = "Mary likes apple and cherry"

documents = [document1, document2]
tfidf_scores = calculate_tfidf(documents)

# Print TF-IDF scores
for word, scores in tfidf_scores.items():
    print(f"{word}: {scores}")