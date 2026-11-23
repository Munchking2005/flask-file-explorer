from flask import Flask, render_template
import os
app=Flask(__name__)
@app.route("/")
def home():
	current_directory=os.getcwd()
	script_location=os.path.abspath(__file__)
	project_directory=os.path.dirname(script_location)
	relative_file="documents/notes.txt"
	absolute_file=os.path.abspath(relative_file)
	return render_template("home.html",
current_directory=current_directory,
script_location=script_location,
project_directory=project_directory,
relative_file=relative_file,
absolute_file=absolute_file)
@app.route("/explore")
def explore():
	project_directory=os.path.dirname(os.path.abspath(__file__))
	contents=os.listdir(project_directory)
	folders=[]
	files=[]
	EXCLUDED_ITEMS={".env",".git","venv","__pycache__",".pytest_cache"}
	for i in contents:
		if i in EXCLUDED_ITEMS:
			continue
		full_path=os.path.join(project_directory,i)
		if os.path.isdir(full_path):
			folders.append(i)
		elif os.path.isfile(full_path):
			files.append(i)
	return render_template("explorer.html",
project_directory=project_directory,
folders=folders,
files=files)
	

if __name__=="__main__":
	app.run(debug=True)

