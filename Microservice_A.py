# Author: Natasha Pavelek
# Date: May 2nd 2024 --> May 5th

import random
import colorsys
from flask import *

HOST = "localhost"
PORT = 2133

app = Flask(__name__)

@app.route('/v1/random_hex')
def random_hex():
    """Given a color category, will generate a random hex value"""

    category = request.args.get('category')
    # if there is a category, use it, else, generate randomly

    if category:
        category = category.upper()

    # base case
    min_hue = 0
    max_hue = 360
    min_sat = 0
    max_sat = 1
    min_value = 0
    max_value = 1

    # Filtering by category:
    if category == 'RED':
        min_hue = 0
        max_hue = 20
        min_sat = 0.25
        max_sat = 1
        min_value = 0.2
        max_value = 1
    elif category == 'ORANGE':
        min_hue = 19
        max_hue = 40
        min_sat = 0.25
        max_sat = 1
        min_value = 0.2
        max_value = 0.8
    elif category == 'YELLOW':
        min_hue = 35
        max_hue = 70
        min_sat = 0.30
        max_sat = 1
        min_value = 0.3
        max_value = .9
    elif category == 'GREEN':
        min_hue = 80
        max_hue = 120
        min_sat = 0.25
        max_sat = 1
        min_value = 0.2
        max_value = .9
    elif category == 'BLUE':
        min_hue = 180
        max_hue = 220
        min_sat = 0.2
        max_sat = 1
        min_value = 0.2
        max_value = .9
    elif category == 'PURPLE':
        min_hue = 260
        max_hue = 300
        min_sat = 0.2
        max_sat = 1
        min_value = 0.2
        max_value = .9

    hue = random.uniform(min_hue / 360, max_hue / 360)
    # need to implement a wrap around for red to include purple reds
    saturation = random.uniform(min_sat, max_sat)
    value = random.uniform(min_value, max_value)
    # this is good when I am ready to filter by shade, but may conflict with microservice
    # anchor when ready and fall back on offset

    red, green, blue = colorsys.hsv_to_rgb(hue, saturation, value)
    # color conversions - pretty sure imports are valid per syllabus
    red = int(red * 255)
    green = int(green * 255)
    blue = int(blue * 255)

    hex_color_str = '#' + f'{red:02x}{green:02x}{blue:02x}'
    std_color = hex_color_str

    print(str(category) + ' = ' + str(std_color))

    response = make_response(std_color)
    response.headers.add('Access-Control-Allow-Origin', '*')
    # this allows the browser to access my code (do not delete)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
