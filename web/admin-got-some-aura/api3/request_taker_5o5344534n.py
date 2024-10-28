from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return "available_endpoints-\n /api/fetch_local - fetches data from local URLs and APIs"

@app.route('/api/fetch_local', methods=['POST'])
def fetch_local_data():
    form_data = request.form
    target_url = form_data.get('likeAPI')
    
    if not target_url:
        return jsonify({"error": "No URL provided"}), 400
    elif target_url=='http://iitbtrustlab-ssrf.chals.io:3020' or target_url=='http://iitbtrustlab-ssrf.chals.io:3020/':
        return "available_endpoints- \n /api/get_likes - get aura of registered users"
    
    elif target_url == 'http://iitbtrustlab-ssrf.chals.io:3020/api/get_likes?username=hritik':
        return jsonify({"Aura": "500000"}), 200
    elif target_url == 'http://iitbtrustlab-ssrf.chals.io:3020/api/get_likes?username=arjun':
        return jsonify({"Aura": "73(Bro really starred in 'the Ladykiller')"}), 200
    elif target_url == 'http://iitbtrustlab-ssrf.chals.io:3020/api/get_likes?username=cilian':
        return jsonify({"Aura": "500001"}), 200
    elif target_url == 'http://iitbtrustlab-ssrf.chals.io:3020/api/get_likes?username=Aayush':
        return jsonify({"Aura": "8358745698345698345973587346534657"}), 200
    elif target_url.startswith('http://iitbtrustlab-ssrf.chals.io:3020/api/get_likes?'):
        return jsonify({"Error":"user not found!"}), 200
    
    elif target_url == 'http://iitbtrustlab-ssrf.chals.io:3064/' or target_url == 'http://iitbtrustlab-ssrf.chals.io:3064':
        return "available_endpoints- \n/api/admin-access - wait, you should not have access to this endpoint!!"
    elif target_url == 'http://iitbtrustlab-ssrf.chals.io:3064/api/admin-access':
        return "tyroCTF{s5rf_4ll_1he_w4y}"
    elif target_url.startswith('http://iitbtrustlab-ssrf.chals.io:3064'):
        return jsonify({"error": "Invalid endpoint"}), 400
    else:
        return jsonify({"error": "Invalid URL"}), 400
        

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)




    # try:
    #     # Fetch the data from the provided URL
    #     response = requests.get(target_url)
    #     response.raise_for_status()  # Raise an error for bad status codes
        
    #     # Return the content of the response
    #     content = response.json() 
        
    #     return content["Aura"], 200

    # except requests.exceptions.RequestException as e:
    #     return jsonify({"error": f"Failed to fetch the data: {str(e)}"}), 500

