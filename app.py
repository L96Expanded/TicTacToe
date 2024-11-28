from flask import Flask, request, jsonify, render_template
import json
import os

# starts the python server and holds the function to let 'main.js' get and modify 'data.json'


# creates the Flask app
app = Flask(__name__)

# Path to the JSON file
json_file = 'data.json'

# routes the website to automatically display the 'index.html' file 
@app.route('/')
def index():
    """
    Displays the 'index.html' file

    Time Complexity:
    - Best Case: O(1).
    - Average Case: O(1).
    - Worst Case: O(1).
    """
    
    return render_template('index.html')

# Get a fetch 'GET' in the main.js with the name '/get_json_data' 
# request is done this rerouts it to this function (get_json_data())  
@app.route('/modify_json', methods=['POST'])
def modify_json():
    """
    Modifies a specific value within 'data.json'

    Time Complexity:
    - Best Case: O(1).
    - Average Case: O(1).
    - Worst Case: O(1).
    """
    if request.is_json:

        data = request.get_json()
        key = data.get('key')
        value = data.get('value')

        if key and value:

            if os.path.exists(json_file):
                f = open(json_file)
                with open('data.json') as a:
                    data = json.load(f)

                json_content = data
            else:

                json_content = {}

            json_content[key] = value

            with open(json_file, 'w') as file:
                json.dump(json_content, file, indent=4)

            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'error', 'message': 'Missing key or value'}), 400
    else:
        return jsonify({'status': 'error', 'message': 'Request must be JSON'}), 400
    
    
# Get a fetch 'GET' in the main.js with the name '/get_json_data' 
# request is done this rerouts it to this function (get_json_data())  
@app.route('/get_json_data', methods=['GET'])
def get_json_data():
    """
    returns the data inside the 'data.json' file as a json

    Time Complexity:
    - Best Case: O(1).
    - Average Case: O(1).
    - Worst Case: O(1).
    """
    if os.path.exists(json_file):

        with open('data.json') as a:
            data = json.load(a)
        return json.dumps(data)
        
# Runs the app
if __name__ == '__main__':
    app.run(debug=False)
