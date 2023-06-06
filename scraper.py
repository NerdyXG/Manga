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
num_of_manga = 0
manga_list = soup.find_all("div", class_="entry")
for manga in manga_list:
	try:
		manga_title = manga.find("h3", class_="name").a.text
		manga_thumbnail = manga.find("a", class_="thumb").img["src"]
	except AttributeError:
		...
	else:
		print(f"Title: {manga_title}\nThumbnail: {manga_thumbnail}\n")
		num_of_manga += 1

print(f"{num_of_manga} issues scraped!!!")