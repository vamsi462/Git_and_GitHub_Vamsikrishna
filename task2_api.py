import os

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)
MONGO_URI = os.getenv("MONGO_URI")


@app.route("/", methods=["GET", "POST"])
def submit_form():
    if request.method == "POST":
        user_data = request.form.get("user_data")
        try:
            client = MongoClient(MONGO_URI)
            db = client["test_database"]
            collection = db["test_collection"]
            collection.insert_one({"data": user_data})
            return redirect("/success")
        except Exception as e:
            return render_template("index.html", error="Database error: " + str(e))

    return render_template("index.html")


@app.route("/success")
def success():
    return "<h1>Data submitted successfully</h1>"


@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No JSON data provided"})

        item_name = data.get("itemName")
        item_description = data.get("itemDescription")
        item_id = data.get("itemId")
        item_uuid = data.get("itemUuid")
        item_hash = data.get("itemHash")

        client = MongoClient(MONGO_URI)
        db = client["test_database"]
        collection = db["test_collection"]

        collection.insert_one(
            {
                "itemName": item_name,
                "itemDescription": item_description,
                "itemId": item_id,
                "itemUuid": item_uuid,
                "itemHash": item_hash,
            }
        )

        return jsonify({"message": "Item added successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
