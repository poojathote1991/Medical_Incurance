from flask import Flask,request,jsonify,render_template,redirect,url_for
from util import get_predicted_price
import config
import sys
import pandas as pd 
import os 
import re
import traceback
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("medical_insurance1.html")

@app.route('/predict_charges',methods=['GET','POST'])
def predict_charges():
    try:
        if request.method=="GET":
            data=request.args.get
            print("Data: ",data)
            age=int(data('age'))
            gender=data('gender')
            bmi=eval(data('bmi'))
            children=int(data('children'))
            smoker=data('smoker')
            region=data('region')

            pred_price=get_predicted_price(age,gender,bmi,children,smoker,region)
            return render_template("medical_insurance1.html",prediction=pred_price)
        elif request.method=="POST":

            data=request.form
            print("Data: ",data)
            age=data['age']
            gender=data['gender']
            bmi=data['bmi']
            children=data['children']
            smoker=data['smoker']
            region=data['region']

            pred_price=get_predicted_price(age,gender,bmi,children,smoker,region)
            return render_template("medical_insurance1.html",prediction=pred_price)
    except:
        return print(traceback.print_exc())
if __name__=="__main__":
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)