import wikipediaapi
import time
import sys


wiki_wiki = wikipediaapi.Wikipedia('CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)', "ru")

start_page = wiki_wiki.page("Философия")

def print_links(page):
        links = page.links
        for title in links.keys():
            yield("%s: %s" % (title, links[title]))

for i in print_links(start_page):
      print(i)






