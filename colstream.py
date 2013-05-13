from flask import render_template, request, jsonify

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from __init__ import app, my_app
from Playlist import playlist

@app.route('/')
def show_entries():
    return render_template('show_entries.html', entries=playlist)


@app.route('/addsong')
def add_song():
    idsong = request.args.get('idsong', type=int)
    if(idsong == None):
        return jsonify(result="NOK"), 404
    playlist.append(idsong)
    return jsonify(result="OK")


if __name__ == '__main__':
    http_server = WSGIServer(('',8000), my_app, handler_class=WebSocketHandler)
    http_server.serve_forever()