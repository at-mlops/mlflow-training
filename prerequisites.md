# Prerequisites

Please follow the prerequiste steps in the given order and get back in case there are any questions.

## Clone repository

Please clone the [MLflow training repository](https://github.com/at-mlops/mlflow-training) to your local machine `git clone https://github.com/at-mlops/mlflow-training.git`. For the training itself you can user either a .ipynb or .py files. Please choose your preference and make sure you have a suitable IDE already installed.

## Set-Up environment

To set up you environment for the training, follow the following steps. The `requirements.txt` also includes mlflow and other packages relevant for the training. Please note that Python version >=3.8 is required to run smoothly.

Optional:
* You may want to install Jupyter or Jupyter Lab if you prefer working with `.ipynb` files over `.py` scripts for the tasks. You can solve all tasks using our prepared notebooks or Python files.
* In part 4, there is an example that requires `conda` in your PATH in order to run.

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

## Test MLflow installation

Before running MLflow, you may want to create a new directory in this repo, for example called "server" and navigate to this directory before running MLFlow. The `mlflow ui` command creates some new folders and files in whatever directory it is executed so having an extra directory might be cleaner. This step is optional.

Now, test successful installation of MLflow by running `mlflow ui` and access the UI via your browser under `localhost:5000`. In case you are running on Mac, your port 5000 may be occupied. In this case you can [attempt to relase port 5000](https://stackoverflow.com/questions/72369320/why-always-something-is-running-at-port-5000-on-my-mac) or you need to run mlflow on another port, for example `mlflow ui -p 5008`. Keep in mind which port you choose as you need to set a tracking URI for MLflow during the later training steps.

Abort running Mlflow by `ctrl-c`.
