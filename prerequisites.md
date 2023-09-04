# Prerequisites

Please follow the prerequiste steps in the given order and get back in case there are any questions.

## Clone repository

Please clone the [MLflow training repository](https://github.com/at-mlops/mlflow-training) to your local machine `git clone https://github.com/at-mlops/mlflow-training.git`. For the training itself you can user either a .ipynb or .py files. Please choose your preference and make sure you have a suitable IDE already installed.

## Set-Up environment

To set up you environment for the training, follow the following steps. The `requirements.txt` also includes mlflow and other packages relevant for the training. Please note that Python version >=3.8 is required to run smoothly.

### unix/ macOS 
```bash
# switch to the directory where you cloned the repository to
cd mlflow-training

# Creating a virtual environment
python3 -m venv env

# Activating a virtual environment
source env/bin/activate

which python
# should be in .../env/bin/python

# Installing packages
python3 -m pip install -r requirements.txt

# Leaving the virtual environment
# NOTE: obviously we want to keep it activated during the training
deactivate
```

### Windows

```bash
# switch to the directory where you cloned the repository to
cd mlflow-training

# Creating a virtual environment
py -m venv env

# Activating a virtual environment
.\env\Scripts\activate

where python
# should be in ...\env\Scripts\python.exe

# Installing packages
py -m pip install -r requirements.txt

# Leaving the virtual environment
# NOTE: obviously we want to keep it activated during the training
deactivate
```

## Install & Test MLflow

Please install MLflow locally using `pip install MLflow`. In case you have done the previous step on setting up your environment, you have already done this.
Test whether it works by running `mlflow ui` and access the user interface via your browser under `localhost:5000`. In case you are running on Mac, your port 5000 is likely occupied (..by mac control center - wtf why is that listening to ports?...), so you need to run mlflow on another port. Try `mlflow ui -p 5008` for example. Keep in mind which port you choose as you need to set a tracking uri for MLflow during the later training steps.

Abort running Mlflow by `ctrl-c`.
