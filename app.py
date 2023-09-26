from flask import Flask, redirect,render_template,request , url_for
from src.mlproject.pipeline.prediction import PredictionPipeline
from datetime import  datetime
from src.mlproject import logger
import numpy as np
import os
import yaml

obj = PredictionPipeline()

app = Flask(__name__)



@app.route('/', methods=['GET'])
def home_page():
    return render_template('home.html' , current_time =datetime.utcnow())

@app.route('/train', methods=['GET','POST'])
def training():
    os.system('python main.py')
    return 'Training successful<br><form action="/" method="get"><button type="submit">Back to Prediction Page</button></form>'




@app.route('/process_parameters', methods=['GET','POST'])
def Change_parameters():
    try:
        if request.method == 'POST':
            alpha = float(request.form['alpha'])
            l1_ratio = float(request.form['l1_ratio'])

             # Read the existing params.yaml file
            with open('params.yaml', 'r') as yaml_file:
                params = yaml.safe_load(yaml_file)

            # Update the specific values in the params dictionary
            params['ElasticNet']['alpha'] = alpha
            params['ElasticNet']['l1_ratio'] = l1_ratio

            # Write the updated params dictionary back to params.yaml
            with open('params.yaml', 'w') as yaml_file:
                yaml.dump(params, yaml_file, default_flow_style=False)

            # Redirect to the home page after updating parameters
            return redirect(url_for('training'))  # You can render the form again for GET requests
        return render_template('parameters.html')

    except Exception as e:
        return str(e)


@app.route('/predict', methods = ['POST'])
def predict():
    try:            
        if request.method == 'POST':
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