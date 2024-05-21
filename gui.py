# Author: Natasha Pavelek
# Date: May 2nd 2024 --> May 5th

import json
import urllib.request

from flask import *

PORT = 2130

MICROSERVICE_A_HOST = 'localhost'
MICROSERVICE_A_PORT = 2133

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')


@app.route('/random_hex')
def random_hex():
    """Given a color category, will generate a random hex value"""
    url_str = 'http://' + MICROSERVICE_A_HOST + ':' + str(MICROSERVICE_A_PORT) + '/v1/random_hex'
    category = request.args.get('category')
    if category:
        url_str = url_str + '?category=' + category
    with urllib.request.urlopen(url_str) as url:
        data = json.load(url)
        response = make_response(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


@app.route('/')
@app.route('/index.html')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
