# Mlflow-training

![](https://mlflow.org/docs/latest/_static/MLflow-logo-final-black.png)

This repository contains the AT-internal Mlflow training materials. The training is based on the official [MLflow](https://mlflow.org/docs/latest/index.html) documentation.

# Prerequisites

Please follow the prerequiste steps in the given order and get back in case there are any questions.

## Clone repository

Please clone the [MLflow training repository](https://github.com/at-mlops/mlflow-training) to your local machine `git clone https://github.com/at-mlops/mlflow-training.git`. If you do not have any IDE installed or you do not work with an IDE that supports jupyter notebooks we preinstalled jupyter lab for you. 

## Set-Up environment

To set up you environment for the training, follow the following steps. The `pyproject.toml` also includes mlflow and other packages relevant for the training. Please note that Python version >=3.11,<3.12 is required to run smoothly.

```bash
# switch to the directory where you cloned the repository to
cd mlflow-training

# install poetry 
pip install --upgrade poetry 

# create poetry env in project 
poetry install 

# [Optional] for jupyter lab please install the kernel 
poetry shell 
python -m ipykernel install --user --name=mlflow-training

# [Optional] you can access jupyter lab with the command 
jupyter lab 
```

Now you should be able to select the right kernel for your IDE and jupyter notebooks: `mlflow-training` or `.venv`

## Test installation

<b>[Optional]</b>  
Before running MLflow, you may want to create a new directory in this repo, for example called "server" and navigate to this directory before running MLFlow. The `mlflow ui` command creates some new folders and files in whatever directory it is executed so having an extra directory might be cleaner. This step is optional.

<b>[Step 1]</b>    
Now, test successful installation of MLflow by running `mlflow ui` and access the UI via your browser under `localhost:5000`. In case you are running on Mac, your port 5000 may be occupied. In this case you can [attempt to relase port 5000](https://stackoverflow.com/questions/72369320/why-always-something-is-running-at-port-5000-on-my-mac) or you need to run mlflow on another port, for example `mlflow ui -p 5008`. Keep in mind which port you choose as you need to set a tracking URI for MLflow during the later training steps.

<b>[Step 2]</b>
Test if all other packages were installed correctly by executing: 

```shell 
# test venv 
poetry shell 
python src/mlflow_training/test_env.py
```

You should see the message `everything looks good - setup finished!`

If you are struggling with any of the exercises you can checkout the branch `solution` to get hints on how the exercises work. 

# Contributing

If you want to contribute to the training or give your feedback, please reach out to the MLOps Track or your trainers.

