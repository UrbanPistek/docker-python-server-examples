import os
import time
import platform
from flask import Flask, request, jsonify

app = Flask(__name__)

APP_PORT = os.getenv('APP_PORT', 7711)
APP_ROUTES = [
 "/",
 "/routes",
 "/sample_get",
 "/sample_post",
]


@app.route('/') 
def home():
    """
    The base endpoint.
    """
    return 'A sample flask-gunicorn server'


@app.route('/routes', methods=['GET'])
def routes():
    """
    Returns a list of all the routes availible on this service.
    """
    response = {
        "routes": APP_ROUTES
    }
    return jsonify(response), 200 


@app.route('/sample_get', methods=['GET'])
def sample_get():
    """
    A simple GET route. 
    """
    os_name:str = platform.system()
    os_release:str = platform.release()
    os_architecture:str = platform.architecture()[0]
    response = {
        "unix_ts": time.time(),
        "os_name": os_name,
        "os_release": os_release,
        "os_architecture": os_architecture
    }
    return jsonify(response), 200


@app.route('/sample_post', methods=['POST'])
def sample_post():
    """
    A simple POST. 
    """
    data = request.get_json()
    msg:str = data.get('msg', '')
    
    response = {
        "msg_received": msg,
        "unix_ts": time.time()
    }
    
    return jsonify(response), 200
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=APP_PORT)
