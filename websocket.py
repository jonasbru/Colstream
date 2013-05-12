# coding: utf-8
import json
import os
import subprocess
import telnetlib


def handle_websocket(ws):
    while True:
        print "plop4"
        message = ws.receive()
        if message is None:
            break
        print "plop5"
        message = json.loads(message)

        ws.send(json.dumps({'output': message['output']}))

        HOST = "localhost"
        tn = telnetlib.Telnet(HOST, 32000, 10000)

        # tn.read_until("login: ")

        print message['output']
        tn.write(message['output'].encode("utf-8") + "\n")

        # tn.write("ls\n")
        # tn.write("exit\n")
        print "plop1"
        print tn.read_until("\n", 3000)
        print "plop2"

        tn.write("window.Grooveshark.getCurrentSongStatus()" + "\n")
        print tn.read_until("\n", 3000)


        tn.close()
        print "plop3"



        
