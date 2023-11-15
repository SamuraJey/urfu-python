from urllib import parse
import re
import requests
import time


class TooManyRedirections(Exception):
    pass

def wikipedia_pathfinder(start_word, end_word, lang):
    history = {start_word: None}
    queue = [start_word]
    request_id = 0
    session = requests.Session()

    while not search_on_next_page(start_word, end_word, lang, history, queue, request_id, session):
        pass

    chain = []
    word = end_word
    while word is not None:
        chain.append(word)
        word = history[word]

    chain.reverse()
    print('Shortest path:', ' -> '.join(chain))


def search_on_next_page(start_word, end_word, lang, history, queue, request_id, session):
    request_id += 1
    if request_id > 2000:
        raise TooManyRedirections("Too many medirections (over 2000)")
    word = queue.pop(0)

    debug_info = f'{len(history)}, {request_id}, {word}'

    r = session.get(url=f'https://{lang}.wikipedia.org/wiki/{word}')

    pattern = re.compile(r'href="/wiki/([^:#"]+)"') # Всё кроме символов :#"
    links = (parse.unquote_plus(href) for href in pattern.findall(r.text))

    for href in links:
        if href not in history:
            history[href] = word
            if href == end_word:
                return True
            queue.append(href)
    # print(f'{debug_info}')


def main():
    start_word = "Философия"
    end_word = "Машина"
    lang = "ru"

    start_time = time.time()
    wikipedia_pathfinder(start_word, end_word, lang)
    end_time = time.time()
    print(round(end_time - start_time, 3))


if __name__ == '__main__':
    main()