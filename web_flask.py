from flask import Flask, render_template
import get_data
app = Flask(__name__)


@app.route("/")
def hello():
    artists = get_data.get_all_artist()
    return render_template("index.html", artists=artists)


@app.route("/songs/<int:aid>")
def list_all_songs(aid):
    songs = get_data.get_all_songs(aid)
    artist = get_data.singer(aid)
    artists = get_data.get_all_artist()
    return render_template("songlist.html", artist=artist, artists=artists, songs=songs, current=aid)


@app.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyrics(sid, aid):
    songs = get_data.get_all_songs(aid)
    artist = get_data.singer(aid)
    artists = get_data.get_all_artist()
    lyrics = get_data.get_lyrics(sid)
    return render_template("lyrics.html", lyrics=lyrics, artist=artist, artists=artists, songs=songs)


if __name__ == "__main__":
    app.run(debug=True)
