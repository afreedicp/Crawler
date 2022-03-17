import requests
import os
from bs4 import BeautifulSoup


def get_songs(artist_url):
    songs = []
    r = requests.get(artist_url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    tracklist = soup.find("table", {"class": "tracklist"})
    link = tracklist.find_all("a")
    for i in link:
        songs.append((i.text, i["href"]))
    return songs


def get_lyrics(song_url):
    r = requests.get(song_url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    lyrics_div = soup.find("p", {"id": "songLyricsDiv"})
    lyrics = lyrics_div.text
    return lyrics


def get_artists(url):
    ret = []
    r = requests.get(url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    tracklist = soup.find("table", {"class": "tracklist"})
    link = tracklist.find_all("a")
    for i in link:
        ret.append((i.text, i['href']))
    return ret


def crawl():

    artist = get_artists("http://www.songlyrics.com/l/")
    for name, link in artist:
        songs = get_songs(link)
        for song, song_link in songs:
            print("-------------------------------------------------------------", song, name,
                  "-----------------------------------------")
            lyrics = get_lyrics(song_link)
            print(lyrics)
            print("\n")
    print("DONE")


if __name__ == "__main__":
    crawl()
