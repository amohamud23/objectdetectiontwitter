from flask import Flask, render_template, request, redirect
import requests
app = Flask(__name__)
import pickle
import json

@app.route('/')
def home():
    
    return render_template('index.html')
@app.route('/upload', methods = ['GET', 'POST'])
def sendImage():
    if request.method == 'POST':
        print("sending image")
        img = request.files['myfile']
        files = {'file': img.read()}
        URL = "http://aba3b077.ngrok.io/"
        r = requests.get(url=URL, files=files)
        j = json.loads(r.text)
        print(j)
    return redirect('/')


if __name__ =="__main__":
    app.run(debug=True)