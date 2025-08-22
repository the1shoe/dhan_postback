from flask import Flask, request

app = Flask(__name__)

@app.route('/dhan-postback', methods=['POST'])
def dhan_postback():
    data = request.json
    print("🔔 Postback received:", data)
    return "OK", 200
