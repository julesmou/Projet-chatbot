from re import X
from flask import Flask, render_template, jsonify
from flask import request
import os
import pprint as p

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static','IMG')



# @app.route('/')
@app.route('/')
def photo():
    filename=request.args.get('filename')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], f'{filename}.jpg')
    return render_template('index.html', user_image=full_filename
                       )
# import webbrowser
# webbrowser.open("http://127.0.0.1:5000?filename=chiens")

# /index?photo=out.png