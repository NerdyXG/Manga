"""
REQUIREMENTS:
	~ For the first phase, simple display the name and the thumbnail for each manga
	~ When a specific manga is selected:
		~ Display the list of chapters available for that particular manga (links)?
		~ When the user clicks on the download button, the entire chapter should be downloaded into a file
		~ Save the file with that specific chapter name
		~ There should also be an option to read the manga live on the app without downloading it.
"""


from bs4 import BeautifulSoup as bs
import requests, sys, urllib.request, wget

print("Connecting to server...\n")

try:
    html_data = requests.get("https://w31.holymanga.net/manga-list/").text
except requests.exceptions.RequestException as err:
    sys.exit(err)

soup = bs(html_data, "lxml")
manga_list = soup.find("div", class_="entry")
manga_title = manga_list.find("h3", class_="name").a.text
manga_thumbnail = manga_list.find("a", class_="thumb").img["src"]
print(manga_thumbnail)