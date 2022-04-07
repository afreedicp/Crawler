from flask import Flask, render_template, jsonify
import get_data
app = Flask(__name__)


@app.route("/afreedi")
def x():
    return "Hello! There!"


@app.route("/")
def hello():
    return render_template("base.html")


@app.route("/artist")
def get_artist():
    artists = get_data.get_all_artist()
    artist_arr = [{'id': i[0], "name":i[1]} for i in artists]
    return jsonify(artist_arr)


@app.route("/songs/<int:aid>")
def list_all_songs(aid):
    songs = get_data.get_all_songs(aid)
    songs_arr = [{'id': i[0], "name":i[1]} for i in songs]
    return jsonify(songs_arr)


@app.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyrics(sid, aid):
    songs = get_data.get_all_songs(aid)
    artist = get_data.singer(aid)
    artists = get_data.get_all_artist()
    lyrics = get_data.get_lyrics(sid)
    return render_template("lyrics.html", lyrics=lyrics, artist=artist, artists=artists, songs=songs)


if __name__ == "__main__":
    app.run(debug=True)
