import psycopg2


def get_all_artist():
    conn = psycopg2.connect("dbname=music")
    cur = conn.cursor()
    cur.execute("select id,name from artist")
    artists = cur.fetchall()
    return artists


def get_all_songs(aid):
    conn = psycopg2.connect("dbname=music")
    cur = conn.cursor()
    cur.execute(
        "select song.name, song.songid from song,artist where artist.id = song.artist and artist.id=%s", (aid,))
    songs = cur.fetchall()
    return songs


def get_lyrics(sid):
    conn = psycopg2.connect("dbname=music")
    cur = conn.cursor()
    cur.execute("select lyrics,name from song where songid=%s", (sid,))
    lyric = cur.fetchone()
    return lyric


def singer(artistid):
    conn = psycopg2.connect("dbname=music")
    cur = conn.cursor()
    cur.execute("select id,name from artist where artist.id=%s", (artistid,))
    singer = cur.fetchone()
    return singer
