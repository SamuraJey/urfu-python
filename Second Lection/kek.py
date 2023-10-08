import re

def extract_words(text):
    # Используем регулярное выражение для удаления символов, не являющихся буквами
    # и разделяем строку на слова
    words = re.findall(r'\b\w+\b', text.lower())
    return words

# Пример использования
input_text = "Привет! Как дела? Я - робот."
words = extract_words(input_text)
print(words)