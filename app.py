from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
	return "<h1>Not gonna lie this ain't my first tango</h1>"
if __name__=="__main__":
	app.run(debug=True)

