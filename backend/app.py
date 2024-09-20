#Dependencies 
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from model import fetch_strava_data, preprocess_strava_data, format_query, generate_advice


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
# # #CORS allows request from localhost 3000 / React app location
# CORS(app, resources={r"/api/*": {
#         "origins": "http://localhost:3000",
#         "methods": ["GET", "POST", "OPTIONS"],
#         "allow_headers": ["Content-Type"]
#     }})



@app.route('/advice', methods=['OPTIONS', 'GET', 'POST'])
def advice(): 

    if request.method == 'OPTIONS':
        # Preflight request
        response = Response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    elif request.method == 'GET':
        return 'Here is some advice'
    elif request.method == 'POST':
        data = request.json
        prompt = data.get('prompt', '')
        if prompt == '':
            print('No prompt given')
            return jsonify({'error': 'No prompt provided'}), 400
        advice = "Sample advice "
        message = advice + prompt
        return jsonify({"message": message})
    

    


#when post request comes through go to advice function
# @app.route('/advice', methods=['POST'])
# def get_advice(): 

    #Get JSON data from incoming request
    # data = request.json
     
    # prompt = data.get('prompt', '')

    # access_token = data.get('access_token')

    # if not access_token: 
        #The HTTP 400 Bad Request client error  indicates that the server would not process the request due to something the server considered to be a client error.
        # return jsonify({'error': 'Access Token is required'}), 400

    # if prompt == '': 
    #     print('No prompt given')
    # else: 
    #     return

    # advice = "Sample advice "
    # message = advice + prompt

    # return jsonify({"message": message})



    # try: 
           # Fetch and process Strava data
        # strava_data = fetch_strava_data(access_token)
        # processed_data = preprocess_strava_data(strava_data)
        # query = format_query(processed_data)



            # Generate and return advice
        # advice = generate_advice(query)
        # advice = "Placeholder advice"
        # return jsonify({"advice": advice})


    # except Exception as e: 
    #     return jsonify({"error": str(e)}), 500



#Name is set to main if the script is being run directily as opposed to imported in
if __name__ == '__main__':
    #Run the script
    app.run(debug=True, port=5000)

 