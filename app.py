# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:47:29 2020

@author: Ratan Singh
"""

from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = "static/uploads"


@app.route("/")
def home():
    return render_template("c2-benchmark.html")


@app.route("/bonds")
def bonds():
    return render_template("databond.html")


@app.route("/loans")
def loans():
    return render_template("loan.html")


@app.route("/fx")
def fx():
    return render_template("fx.html")


@app.route("/fospread")
def fospread():
    return render_template("fospread.html")
    

@app.route('/fileUpload')
def upload_file():
   return render_template('file-upload.html')


@app.route('/proxy')
def proxyBasket():
    return render_template('proxy-basket.html')
    

@app.route('/criteria')
def proxyCriteria():
    return render_template('proxy-criteria.html')


@app.route('/averages')
def averages():
    return render_template('averages.html')


@app.route('/curves')
def curves():
    return render_template('benchmark-curves.html')
    

@app.route('/report')
def report():
    return render_template('benchmark-report.html')
	

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      files = ['marketbond', 'loan', 'fx', 'fospread', 'proxy']
      for fileName in files:
          try:
              f = request.files[fileName]
              f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
          except:
              pass
   return redirect('/fileUpload')


@app.route('/loanId')
def loanId():
    return {"loanId" : ["Loan 1", "Loan 2"]}

@app.route('/data')
def data():
    return pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], "Data.csv")).to_json(orient = 'split')

@app.route("/about")
def about():
    return render_template("c2-benchmark.html")
    
if __name__ == "__main__":
    app.run(debug=True)