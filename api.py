from flask import Blueprint, jsonify
import get_data
api = Blueprint('api', __name__)


@api.route("/artist")
def get_artist():
    artists = get_data.get_all_artist()
    artist_arr = [{'id': i[0], "name":i[1]} for i in artists]
    return jsonify(artist_arr[0])


@api.route("/songs/<int:aid>")
def get_songs(aid):
    songs = get_data.get_all_songs(aid)
    songs_arr = [{'id': i[1], "name":i[0]} for i in songs]
    return jsonify(songs_arr)


@api.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyrics(sid, aid):
    lyrics = get_data.get_lyrics(sid)
    songs = get_data.get_all_songs(aid)
    return jsonify(lyrics)
