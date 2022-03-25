import requests
from bs4 import BeautifulSoup
import psycopg2


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
    conn = psycopg2.connect("dbname=music")
    curr = conn.cursor()
    curr.execute(
        'ALTER SEQUENCE ARTIST_id_seq RESTART WITH 1')
    curr.execute(
        'ALTER SEQUENCE SONG_songid_seq RESTART WITH 1')
    curr.execute('DELETE FROM SONG')
    curr.execute('DELETE FROM ARTIST')
    for name, link, in artist[:10]:
        songs = get_songs(link)
        curr.execute(
            'INSERT INTO ARTIST(Name)VALUES(%s)', (name,))
        for song, song_link in songs[:10]:

            lyrics = get_lyrics(song_link)

            curr.execute(
                'INSERT INTO song(artist,name,Lyrics)VALUES((SELECT id from artist WHERE name=%s),%s,%s);', (name, song, lyrics,))
            print(song,
                  "---")

        # print(lyrics)
        # print("\n")
    conn.commit()
    conn = curr.close()


if __name__ == "__main__":
    crawl()
