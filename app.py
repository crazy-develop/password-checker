from flask import Flask, request, jsonify, render_template
from zxcvbn import zxcvbn

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    password = data.get('password', '')
    result = zxcvbn(password)
    
    response = {
        'score': result['score'],
        'crack_time': result['crack_times_display']['offline_fast_hashing_1e10_per_second'],
        'suggestions': result['feedback']['suggestions'] or ["Strong password!"],
        'warning': result['feedback']['warning']
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
