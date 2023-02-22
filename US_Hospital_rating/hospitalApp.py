import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
import pickle
from flask import Flask, request, render_template, url_for, redirect, session, flash

app = Flask(__name__)  # , static_folder='../static'

with open('hospital_model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')  # , methods=['GET', 'POST']
def home():
    return render_template('index.html')


@app.route('/prediction/', methods=['POST'])
def prediction():
    input_dict = request.form.to_dict()
    print(input_dict)
    input_df = pd.DataFrame(input_dict, index=[1])
    prediction = model.predict(input_df)
    print(prediction)

    return render_template('index.html', prediction=prediction[0])


if __name__ == '__main__':
    app.run(debug=True)
