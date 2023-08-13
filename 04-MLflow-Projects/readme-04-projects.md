# MLflow Projects

MLflow Projects packages data science code in a standard format. This allows reusable, and reproducible code to share with other data scientists, and transfer it to production. A MLflow project might be a local directory or a Git repository. It uses a descriptor file to specify its dependencies and entrypoints.

## Sklearn wine quality

Simple SKlearn ElasticNet Model to classify Wine quality and to demonstrates the different ways to run an MLflow Project. For details see [MLflow documentation - Running Projects](https://mlflow.org/docs/latest/projects.html#running-projects).

#### Setup

Set up the connection to the external tracking server by setting the `MLFLOW_TRACKING_URI` environment variable. MLflow will fetch it automatically.

```bash
export MLFLOW_TRACKING_URI=http://localhost:5008
```

#### Running

There are different ways to run MLflow scripts. Of course, we can run it unmanaged as a plain python file using the command line.

```bash
python hello_world.py
```

Yet, keep in mind we need to set up a proper environment first, and also need to run the MLflow UI... How troublesome... MLFlow Projects are packaged code, they allow you to do everything with one simple command.

```bash
mlflow run .
```

This will create the necessary environment (conda), run the mlflow tracking server, create an experiment if it does not exist, and it will train the model and log everything.

You can also specify an experiment name, or additional parameters (if possibility given in your train.py):
```bash
mlflow run . --experiment-name=local_mlflow_project -P alpha=0.01 -P l1_ratio=0.2
```

Or as mentioned above, don't use a local directory but use as git repository:

```bash
mlflow run https://github.com/mlflow/mlflow-example.git --experiment-name=github_mlflow_project -P alpha=0.03 -P l1_ratio=0.4
```
