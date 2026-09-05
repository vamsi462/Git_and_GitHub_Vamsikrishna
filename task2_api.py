from flask import Flask, redirect, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = "mongodb+srv://krish:12345@cluster0.dnkqm.mongodb.net/?appName=a"


@app.route("/", methods=["GET", "POST"])
def submit_form():
    error_msg = None
    if request.method == "POST":
        user_data = request.form.get("user_data")
        try:
            client = MongoClient(MONGO_URI)
            db = client["test_database"]
            collection = db["test_collection"]
            collection.insert_one({"data": user_data})
            return redirect("/success")

        except Exception:
            error_msg = "Connection failed"

    return render_template("index.html", error=error_msg)


@app.route("/success")
def success():
    return "<h1>Data submitted successfully</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
