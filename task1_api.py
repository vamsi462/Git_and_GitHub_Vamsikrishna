import json

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api", methods=["GET"])
def get_data():
    # reading from the backend json file
    with open("data.json", "r") as file:
        list_data = json.load(file)

    # return response as json
    return jsonify(list_data)


if __name__ == "__main__":
    app.run(debug=True)
