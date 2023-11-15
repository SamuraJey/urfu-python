import httpx

response = httpx.get("https://ru.wikipedia.org/wiki/Философия")
print(response.text)