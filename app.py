#print("Hello World!")
from flask import Flask, render_template, request, redirect, url_for, flash

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

#from flask_uploads import ALL, UploadSet, configure_uploads

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'some_secret_key'

@app.route("/")
def hello_world():
    #return "<p>Hello, World!</p>"
    return render_template('index.html')

if __name__ == '__main__':
  #app.run(debug=True)
  app.run(host='0.0.0.0', debug=True)