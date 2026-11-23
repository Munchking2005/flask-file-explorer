from flask import Flask, render_template_string
import os
app=Flask(__name__)
@app.route("/")
def home():
	current_directory=os.getcwd()
	script_location=os.path.abspath(__file__)
	project_directory=os.path.dirname(script_location)
	relative_file="documents/notes.txt"
	absolute_file=os.path.abspath(relative_file)
	return render_template_string("""
	<h1>Flask Path Explorer</h1>
	<h2>Path information</h2>

	<p><strong>Current working directory :</strong>
	{{current_directory}}
	</p>

	<p><strong>Script_location:</strong>
	{{script_location}}
	</p>
	
	<p><strong>Project directory:</strong>
	{{project_directory}}
	</p>
	
	<p><strong>Relative file path:</strong>
	{{relative_file}}
	</p>
	
	<p><strong>Resolved file path:</strong>
	{{absolute_file }}
	</p>
	
""",
current_directory=current_directory,
script_location=script_location,
project_directory=project_directory,
relative_file=relative_file,
absolute_file=absolute_file)
if __name__=="__main__":
	app.run(debug=True)

