import httpx
import lxml.html
from urllib.parse import unquote

response = httpx.get("https://ru.wikipedia.org/wiki/Философия")
html = lxml.html.fromstring(response.text)
mv_body = html.xpath('//*[@id="mw-content-text"]')[0].xpath('.//a/@href')
answ = [unquote(i) for i in mv_body if i.startswith('/wiki/')]

print(answ)
