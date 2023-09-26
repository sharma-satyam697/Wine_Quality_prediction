# Ml_end_to_end_project 🚀

Welcome to the Machine Learning End-to-End Project with MLOps! In this project, you'll find a comprehensive guide on how to set up, run, and deploy your machine learning model.

## Table of Contents

1. [Workflows](#workflows)
2. [How to Run](#how-to-run)
3. [Mlflow](#mlflow)
4. [Dagshub](#dagshub)
5. [AWS - CI/CD Deployment with GitHub Actions](#aws-cicd-deployment-with-github-actions)

----

## Workflows 📝 
 1. **Update `config.yaml`**
   - Create one stage and go update the config.yaml file.
   - Repeat this step for each stage.
   - These stages represent the full end-to-end project.
   - 1. Data Ingestion
     2. Data Validation
     3. Data Transformation
     4. Model Training
     5. Model Evaluation

2. **Update `schema.yaml`**
   - Guidelines for schema updates.

3. **Update `params.yaml`**
   - Since this project is integrated with MLOps (Dagshub), keep changing the parameters stored in the params.yaml file to track metrics in your MLOps.

4. **Update Files in `src/mlproject/entity`**
   - Create Data Ingestion.
   - - Go to `.config_entity.py` and create the data class for the same.
   - Repeat this for all the stages.

5. **Update the Configuration Manager in `src/config`**
   - Create methods for each stage.
   - Before that, ensure you configure all the data classes in the Configuration class.

6. **Update the `components/__init__.py` File in `src/mlproject`**
   - Add paths for the YAML files.

7. **Update the Pipeline in `src/mlproject`**
   - Create pipelines for the respective stages in different files under the `pipeline` directory.

8. **Update `main.py`**
   - Store all the pipelines in the `main.py` file, which is the main file of the project.

9. **Update `app.py`**
   - Add functions to access user input via HTML pages and route them to functions in `app.py`.

## How to Run? 🏃‍♀️

Follow these steps to get started with the project:

1. **Clone the Repository:**
   - `git clone https://github.com/codedestructed007/Ml_end_to_end_project`

2. **Create a Virtual Environment:**
   - `python -m venv <environment_name>`

3. **Activate the Environment:**
   - `<path_to_environment>/Scripts/activate`
   - Make sure you are in the root directory of your project.

4. **Install Requirements:**
   - `pip install -r requirements.txt`

5. **Run `app.py` in Your Terminal:**
   - `python app.py`

6. **Open in Your Browser:**
   Open your browser and navigate to `http://localhost:<port>`.

### Mlflow 📊

To access MLflow UI, run:
```shell
mlflow ui


### Mlflow 📊

To access MLflow UI, run:
  - mlflow ui

## Dagshub 🚀
Explore your project on Dagshub:

MLFLOW_TRACKING_URI=https://dagshub.com/codedestructed007/Ml_end_to_end_project.mlflow \
MLFLOW_TRACKING_USERNAME=codedestructed007 \
MLFLOW_TRACKING_PASSWORD=5780be4d27268796fc9f39b1b123b32d86ba1bac \
python script.py

Run this export as an environment variable:
export MLFLOW_TRACKING_URI=https://dagshub.com/codedestructed007/Ml_end_to_end_project.mlflow
export MLFLOW_TRACKING_USERNAME=codedestructed007
export MLFLOW_TRACKING_PASSWORD=5780be4d27268796fc9f39b1b123b32d86ba1bac


[Documentation](https://mlflow.org/docs/latest/tracking.html)

## AWS - CI/CD Deployment with GitHub Actions ☁️

### Deployment to AWS

1. Log in to AWS Console
2. Create IAM User for Deployment

### Steps
Steps:
Grant EC2 Access: Create a virtual machine (EC2).
Set Up ECR: Use Elastic Container Registry to save your Docker image in AWS

## About the Deployment Process
1. Build Docker Image from the Source Code.
2. Push Your Docker Image to ECR.
3. Launch an EC2 Instance.
4. Pull Your Image from ECR to EC2.
5. Run Your Docker Image in EC

#### Required Policies
1. AmazonEC2ContainerRegistryFullAccess.
2. AmazonEC2FullAccess.


