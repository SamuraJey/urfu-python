import httpx
import lxml.html
import urllib.parse



response = httpx.get("https://ru.wikipedia.org/wiki/Философия")
html = lxml.html.fromstring(response.text)
mv_body = html.xpath('//*[@id="mw-content-text"]')[0]

links = mv_body.xpath('.//a/@href')

mathem = urllib.parse.quote_plus("Математика")

index = links.index('/wiki/' + mathem)
print(index)




