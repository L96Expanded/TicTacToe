from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Path to the JSON file
json_file = 'data.json'


@app.route('/')
def index():
    # Serve the index.html page
    return render_template('index.html')


@app.route('/modify_json', methods=['POST'])
def modify_json():
    # Check if the request content type is JSON
    if request.is_json:
        # Parse the JSON from the incoming request
        data = request.get_json()
        key = data.get('key')
        value = data.get('value')

        if key and value:
            # Check if the JSON file exists
            if os.path.exists(json_file):
                f = open(json_file)
                with open('data.json') as a:
                    data = json.load(a)
                # json_content = json.load(f)
                json_content = data
            else:
                # If the file doesn't exist, create an empty dict
                json_content = {}

            # Modify or add the key-value pair
            json_content[key] = value

            # Write the updated content back to the JSON file
            with open(json_file, 'w') as file:
                json.dump(json_content, file, indent=4)

            # Return a success response
            return jsonify({'status': 'success'})
        else:
            # If key or value is missing, return an error
            return jsonify({'status': 'error', 'message': 'Missing key or value'}), 400
    else:
        # If the request is not JSON, return an error
        return jsonify({'status': 'error', 'message': 'Request must be JSON'}), 400
    
    
@app.route('/get_json_data', methods=['GET'])
def get_json_data():
    
    if os.path.exists(json_file):

        with open('data.json') as a:
            data = json.load(a)
                # json_content = json.load(f)
        return json.dumps(data)
        



if __name__ == '__main__':
    app.run(debug=False)
