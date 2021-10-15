# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:48:46 2020

@author: KIRAN
"""

from flask import Flask, render_template, request
import pickle

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods =['POST'])
def predict():
    t = request.form['tv']
    r = request.form['r']
    n = request.form['np']
    x = [[float(t),float(r),float(n)]]
    z = (float(t)+float(r)+float(n))
    ypred = model.predict(x)
    if z == 0:
        return render_template("index.html", showcase = "sales: $0")
    else:
        return render_template("index.html",showcase = "sales: $" + str(ypred[0][0]))

if __name__ == '__main__':
    app.run(debug = True)