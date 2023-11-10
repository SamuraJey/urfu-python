from urllib import parse
import re
import requests
import time


class TooManyRedirections(Exception):
    pass


class WikipediaPathfinder:
    def __init__(self, start_word, end_word, lang):
        self.start_word = start_word
        self.end_word = end_word
        self.history = {start_word: None}
        self.queue = [start_word]
        self.request_id = 0
        self.lang = lang
        self.session = requests.Session()

    def search(self):
        while not self.search_on_next_page():
            pass
        chain = []
        word = self.end_word
        while word is not None:
            chain.append(word)
            word = self.history[word]

        chain.reverse()
        print('Shortest path:', ' -> '.join(chain))

    def search_on_next_page(self):
        self.request_id += 1
        if self.request_id > 2000:
            raise TooManyRedirections("Too many medirections (over 2000)")
        word = self.queue.pop(0)

        debug_info = f'{len(self.history)}, {self.request_id}, {word}'

        r = self.session.get(
            url=f'https://{self.lang}.wikipedia.org/wiki/{word}')

        pattern = re.compile(r'href="/wiki/([^:#"]+)"')
        links = (parse.unquote_plus(href) for href in pattern.findall(r.text))

        for href in links:
            if href not in self.history:
                self.history[href] = word
                if href == self.end_word:
                    return True
                self.queue.append(href)
        # print(f'{debug_info}')


def main():
    # start_word = input()
    # end_word = input()
    # lang = input()
    start_word = "Философия"
    end_word = "Битва_при_Мегиддо_(XV_век_до_н._э.)"
    lang = "ru"

    wp = WikipediaPathfinder(start_word, end_word, lang)
    start_time = time.time()
    wp.search()
    end_time = time.time()
    print(round(end_time - start_time, 3))


main()
