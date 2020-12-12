import numpy as np
from flask import Flask, request, render_template
import pickle

app= Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features_list = []
    for x in request.form.values():
        features_list.append(int(x))
    features_array = [np.array(features_list)]
    
    predictVal = model.predict(features_array)
    predictedVal = np.round(predictVal[0],2)
    return render_template('index.html', predict_text = "Employee Salary should be ${}".format(predictedVal))
    
if __name__ == '__main__':
    app.run(debug = True)    

