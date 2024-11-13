from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

@app.route('/reverse', methods=['POST'])
def reverse():
    data = request.get_json()
    reversed_string = data.get("string", "")[::-1]
    return jsonify({"reversed": reversed_string})


if __name__ == "__main__":
    app.run(debug=True)

