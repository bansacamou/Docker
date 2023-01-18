from flask import Flask 
app=Flask(__name__)

@app.route("/")
def index():
    return "Bonjour à tous, je suis en initiation sur docker"


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)