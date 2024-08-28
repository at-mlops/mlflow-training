# Prerequisites

Please follow the prerequiste steps in the given order and get back in case there are any questions.

## Clone repository

Please clone the [MLflow training repository](https://github.com/at-mlops/mlflow-training) to your local machine `git clone https://github.com/at-mlops/mlflow-training.git`. For the training itself you can user either a .ipynb or .py files. Please choose your preference and make sure you have a suitable IDE already installed.

## Set-Up environment

To set up you environment for the training, follow the following steps. The `requirements.txt` also includes mlflow and other packages relevant for the training. Please note that Python version >=3.11,<3.12 is required to run smoothly.

```bash
# switch to the directory where you cloned the repository to
cd mlflow-training

# install poetry 
pip install --upgrade poetry 

# create poetry env in project 
poetry config virtualenvs.in-project true
poetry install 

# test venv 
poetry shell 
python src/mlflow_training/test_env.py
```

Now you should be able to select the right kernel for your IDE and jupyter notebooks: `mlflow-training`

## Test MLflow installation

Before running MLflow, you may want to create a new directory in this repo, for example called "server" and navigate to this directory before running MLFlow. The `mlflow ui` command creates some new folders and files in whatever directory it is executed so having an extra directory might be cleaner. This step is optional.

Now, test successful installation of MLflow by running `mlflow ui` and access the UI via your browser under `localhost:5000`. In case you are running on Mac, your port 5000 may be occupied. In this case you can [attempt to relase port 5000](https://stackoverflow.com/questions/72369320/why-always-something-is-running-at-port-5000-on-my-mac) or you need to run mlflow on another port, for example `mlflow ui -p 5008`. Keep in mind which port you choose as you need to set a tracking URI for MLflow during the later training steps.
