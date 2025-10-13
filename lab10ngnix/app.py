from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def root():
    return jsonify({"msg":"API root"})

@app.route('/hello')
def hello():
    return jsonify({"msg":"Hello from Flask"})

@app.route('/echo', methods=['POST'])
def echo():
    return jsonify({"you_sent": request.get_json(silent=True)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
