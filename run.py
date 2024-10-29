import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    data = []
    try:
        with open(os.path.join(app.root_path, "data", "company.json"), "r") as json_data:
            data = json.load(json_data)
    except FileNotFoundError:
        print("Error: 'data/company.json' file not found.")
        data = []  # or you can set a default value for data
    except json.JSONDecodeError:
        print("Error: 'data/company.json' file is not in valid JSON format.")
        data = []  # or you can set a default value for data

    return render_template("about.html", page_title="About", company=data)

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")

@app.route("/careers")
def careers():  # Make sure this is careers not career
    return render_template("careers.html", page_title="Careers")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
