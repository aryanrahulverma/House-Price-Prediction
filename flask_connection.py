from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('hpp.pkl', 'rb'))

@app.route('/')
def main():
    return render_template('House_price_prediction.html')

@app.route('/Predict', methods=['POST'])
def home():
    #model = joblib.load('finalized_model.sav')
    arr = []
    arr.append(request.form['a'])
    arr.append(request.form['b'])
    arr.append(request.form['c'])
    arr.append(request.form['d'])
    arr.append(request.form['e'])
    arr.append(request.form['f'])
    arr.append(request.form['g'])
    arr.append(request.form['h'])
    arr.append(request.form['i'])
    arr.append(request.form['j'])
    pred = model.predict([arr])
    return render_template('predicted_price.html', data = pred)
    
if __name__ == '__main__':
    app.run(debug=True)