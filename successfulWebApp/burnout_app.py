from flask import Flask, request, render_template, url_for
import jsonify
import requests
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import pickle

app = Flask(__name__)

model = pickle.load(open('polynomial_linearreg2 (5).pkl', 'rb'))

@app.route('/', methods=["GET"])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route('/predict', methods=["POST"])
def predict():
    if request.method == 'POST':
        gender_1 = request.form['gender_1']
        if (gender_1=='Male'):
            gender_1=1
        else:
            gender_1=0
        company_type_1 = request.form['company_type_1']
        if (company_type_1=='Product'):
            company_type_1=1
        else:
            company_type_1=0
        wfh_setup_available_1 = request.form['wfh_setup_available_1']
        if (wfh_setup_available_1=='Yes'):
            wfh_setup_available_1=1
        else:
            wfh_setup_available_1=0
        designation = float(request.form['designation'])
        resource_allocation = float(request.form['resource_allocation'])
        mental_fatigue_score = float(request.form['mental_fatigue_score'])
        inputs = [[gender_1, company_type_1, wfh_setup_available_1, designation, resource_allocation, mental_fatigue_score]]
        prediction = model.predict(inputs)
        output=(round(prediction[0],3)).ravel()
        result=pd.cut(output, bins = 5,labels=['HONEYMOON PHASE', 'ONSET OF STRESS', 'CHRONIC STRESS', 'BURNOUT', 'HABITUAL BURNOUT'])
        #[0., 0.2, 0.4, 0.6, 0.8, 1.]
        l1=[designation, resource_allocation, mental_fatigue_score]
        d1=dict(enumerate(l1))
        for i in l1:
        #d=dict(zip(keys,values))
            if i < 0:
                return render_template('index.html',prediction_texts="Sorry, please check the data entered")
            else:
                return render_template('index.html',prediction_text="Employee is experiencing {}".format(result))                        
          
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

        