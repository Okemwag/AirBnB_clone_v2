from flask import Flask
app = Flask(__name__)
@app.route("/Hello HBNB!")
def hello():
	return "Hello HBNB!";

if __name-- = "__main__":
  app.run(debug=True,host="0.0.0.0",port=5000)
