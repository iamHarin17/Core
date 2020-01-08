import os
import sys
import signal
from pathlib import Path
from wsgiref.simple_server import make_server, demo_app
from wsgi import application

def signal_handler(signal, frame):
    sys.exit(0)

if __name__ == '__main__':
    print("Development server started running....")
    print("Visit:http://localhost:5000/")
    print('Press Ctrl+C to exit')
    signal.signal(signal.SIGINT, signal_handler)
    os.environ['SETTINGS_MODULE'] = 'settings'
    os.environ["FRAMEWORK"] = "view"
    os.environ["PATH"] = str(Path(__file__).parent.absolute())
    with make_server('',5000,application) as server:
        server.serve_forever()

