# Ml_end_to_end_project
Machine Learning end to end project with mlops


## Workflows
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the files under src/mlproject/entity
5. Update the configuration manager in src config
6. Update the components/__init__.py file under src/mlproject
7. Update the pipeline under src/mlproject
8. Update the main.py
9. Update the app.py






# How to run?

## steps:

1. Clone the repository
https://github.com/codedestructed007/Ml_end_to_end_project

2. Create an virtual environment after opening the repository

command-

python -m venv(environment name)

3. Activate the environment 
venv\Scripts\activate

4. Install the requirements

pip install -r requirements.txt

5. run app.py file in your terminal

python app.py

6. Open in your browser with local host and port

### Mlflow

7. mlflow ui

### dagshub

[dagshub](https://dagshub.com/)
MLFLOW_TRACKING_URI=https://dagshub.com/codedestructed007/Ml_end_to_end_project.mlflow \
MLFLOW_TRACKING_USERNAME=codedestructed007 \
MLFLOW_TRACKING_PASSWORD=5780be4d27268796fc9f39b1b123b32d86ba1bac \
python script.py

8. Run this export as evn variable:

export MLFLOW_TRACKING_URI=https://dagshub.com/codedestructed007/Ml_end_to_end_project.mlflow

export MLFLOW_TRACKING_USERNAME=codedestructed007

export MLFLOW_TRACKING_PASSWORD=5780be4d27268796fc9f39b1b123b32d86ba1bac




[Documentation](https://mlflow.org/docs/latest/tracking.html)

