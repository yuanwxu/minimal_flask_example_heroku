import json
from flask import Flask
from serve import get_keywords_api

app=Flask(__name__)

keywords_api = get_keywords_api()


# Define a post method for our API.
@app.route('/extractpackages', methods=['POST'])
def extractpackages():
    """ 
    Takes in a json file, extracts the keywords &
    their indices and then returns them as a json file.
    """
    # the data the user input, in json format
    input_data = request.json

    # use our API function to get the keywords
    output_data = keywords_api(input_data)

    # convert our dictionary into a .json file
    # (returning a dictionary wouldn't be very
    # helpful for someone querying our API from
    # java; JSON is more flexible/portable)
    response = json.dumps(output_data)

    # return our json file
    return response
