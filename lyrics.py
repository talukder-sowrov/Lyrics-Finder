import requests
import re
from bs4 import BeautifulSoup


def getsong():
    artistName = str.lower(input("Enter the name of the artist of the song: \n"))
    songName = str.lower(input("Enter the name of the song from the artist \n"))
    artistName = artistName.split()
    songName = songName.split()
    mergedName = artistName + songName
    linkName = '-'.join(mergedName)

    return linkName


def searchlyrics(linkName):
    lyricsWebsite = requests.get(f'https://genius.com/{linkName}-lyrics')
    lyricsWebsiteHTML = BeautifulSoup(lyricsWebsite.text, 'html.parser')
    rawLyrics = lyricsWebsiteHTML.find('p')
    stringRawLyrics = str(rawLyrics)

    return stringRawLyrics


def createlyrics(stringRawLyrics):
    stringRawLyrics = re.sub('<[^<>]+>', '', stringRawLyrics)

    print('\n')
    print(stringRawLyrics)

    linkName = getsong()
    stringRawLyrics = searchlyrics(linkName)
    createlyrics(stringRawLyrics)