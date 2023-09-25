from flask import Flask, redirect,render_template,request
from src.mlproject.pipeline.prediction import PredictionPipeline
from datetime import  datetime
from src.mlproject import logger
import numpy as np
import os

obj = PredictionPipeline()

app = Flask(__name__)



@app.route('/', methods=['GET'])
def home_page():
    return render_template('home.html' , current_time =datetime.utcnow())

@app.route('/train', methods=['GET'])
def training():
    os.system('python main.py')
    return 'Training successful'


@app.route('/predict', methods = ['POST'])
def predict():
    try:            
        if request.method == 'POST':
            logger.info('this post request has been activated')
            ## data accessig
            fixed_acidity = float(request.form['fixed_acid'])
            volatile_acidity = float(request.form['volatile_acid'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur = float(request.form['free_sulfur'])
            total_sulfur = float(request.form['total_sulfur'])
            density = float(request.form['density'])
            pH = float(request.form['ph'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])
            logger.info('All data has been fetched till now')
            user_input = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur,total_sulfur,density,pH,sulphates,alcohol]
            user_input = np.array(user_input).reshape(1,11)
            logger.info(user_input.shape)
            result = obj.predict(user_input)
            result = result[0]
            result = result * 10       # In percentage
            result = round(result,2)
            logger.info('result variabel has stored the prediciton')
            return render_template('result.html',result= result)
    except Exception as e:

        return 'Something is wrong'
    
    else:
        return render_template('home.html')
        
        
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)