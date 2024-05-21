# Microservice A : Generate a random color (within a color category)

This microservice will respond to a request to generate a random color. It will return the color as an HTML hex format.
This will allow a user to see and generate a color and to filter their generated color by selecting a color category.
This program is implemented in Python using the Flask and Flask-JSON libraries.

## Requirements
Python 3 is required, along with Flask and Flask-JSON. Ensure you have Python 3 and the Flask and Flask-JSON libraries are installed before executing the microservice.

* Python: [https://www.python.org/](https://www.python.org/)
* Flask: [https://pypi.org/project/Flask/](https://pypi.org/project/Flask/) | [https://flask.palletsprojects.com/en/3.0.x/](https://flask.palletsprojects.com/en/3.0.x/)
* Flask-JSON: [https://pypi.org/project/Flask-JSON/](https://pypi.org/project/Flask-JSON/) | [https://github.com/skozlovf/flask-json](https://github.com/skozlovf/flask-json)

## How to programmatically REQUEST data from the microservice
Once the Microservice is running, you can send an HTTP request to the REST API by the following url:

    http://[hostname]/v1/random_hex

Optionally, you can specify a color category to include in the URL:

    http://[hostname]/v1/random_hex?category=[color category]

The following color categories are accepted:

* RED
* ORANGE
* YELLOW
* GREEN
* BLUE
* PURPLE

If the color category is empty, omitted, or not recognized, the microservice, by default, will generate a random color throughout the spectrum.

### Example (in JavaScript):

The following is an example in executing the microservice under localhost with port 2133 (the default).

    const response = await fetch('http://localhost:2133/v1/random_hex');
    const json = await response.json();
    const hexcolor = json.color

## How to programmatically RECEIVE data from the microservice
The color generated is returned to the program as a JSON object with the following properties:

* color; the HTML hex formatted color, unless the server encounters an error
* status; the status code of the returned request
* description; the description of the error message if the request or server encounters an error

The JSON object will be in the following format:

    {
        color: [HTML hex color],
        status: [status code]
    }

The HTML hex color will be of the following format:

    #[red hex from "00" - "ff"][green hex from "00" to "ff"][blue hex from "00" to "ff"]

For example, an HTML hex color of a coral red color, and one possible output of the microservice, is:

    #ff8383

### Example:
To run the microservice, run Python with the microservice as the argument:

    $ python Microservice_A

If you are using a Python vitrual environment, then the following syntax is used:

    $ .\.venv\Scripts\python Microservice_A.py

By default, Microservice_A will occupy port 2133.

An example using JavaScript to fetch from the microservice REST API to obtain a random red color and assign the background color and text to an HTML tag:

    fetch('http://localhost:2133/v1/random_hex?category=RED')
        .then(response => {
            console.log(response);
            return response.json()
        })
        .then(data => {
            console.log(data);
            document.getElementById("color-output").style.backgroundColor = data['color'];
            document.getElementById("color-output-text").innerText = data['color'];
        });

This microservice is maintained by Natasha that works with Nancy's program.

## UML Diagram:
![UML_Diagram](https://github.com/Pavluck/CS361/blob/master/UML_diagram.png?raw=true)

