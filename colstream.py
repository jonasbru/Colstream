from flask import render_template

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from __init__ import app, my_app
from Playlist import playlist

@app.route('/')
def show_entries():

    return render_template('show_entries.html', entries=playlist)





if __name__ == '__main__':
    http_server = WSGIServer(('',8000), my_app, handler_class=WebSocketHandler)
    http_server.serve_forever()