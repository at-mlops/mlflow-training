# Prerequisites

## Install MLflow

Please install MLflow locally using `pip install MLflow`. Test whether it works by running `mlflow ui` and access the user interface via your browser under `localhost:5000`. In case you are running on Mac, your port 5000 is likely occupied, so you need to run mlflow on another port. Try `mlflow ui -p 5008` for example. Keep in mind you need to adjust your tracking uri as well.

### Set-Up environment

To set up you environment for the training, follow the following steps. The `requirements.txt` also includes mlflow and other packages relevant for the training.

#### unix/ macOS 
```bash
# Creating a virtual environment
python3 -m venv env

# Activating a virtual environment
source env/bin/activate

which python
# should be in .../env/bin/python

# Installing packages
python3 -m pip install -r requirements.txt

# Leaving the virtual environment¶
deactivate
```

#### Windowns

```bash
# Creating a virtual environment
py -m venv env

# Activating a virtual environment
.\env\Scripts\activate

where python
# should be in ...\env\Scripts\python.exe

# Installing packages
py -m pip install -r requirements.txt

# Leaving the virtual environment¶
deactivate
```

## Clone repository

Please clone the [MLflow training repository](https://github.com/at-mlops/mlflow-training) to your local machine `git clone https://github.com/at-mlops/mlflow-training.git`. For the training itself you can user either a .ipynb or .py files. Please choose your preference and make sure you have a suitable IDE already installed.


