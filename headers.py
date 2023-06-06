import urllib.request


url_address = "https://cdn.mytoon.net/images/2023/05/13/why-the-king-needs-a-secretary-chapter-99-page-0.jpg"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64 x64)"}

request_ = urllib.request.Request(url_address,None,headers)
response = urllib.request.urlopen(request_)
with open("img.jpg", "wb") as file:
	file.write(response.read())

"""
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}
"""