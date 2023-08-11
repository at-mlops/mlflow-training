# MLflow Tracking

MLflow Tracking is used to log and compare model parameters, code versions, metrics, and artifacts of an ML code. Results can be stored to local files or to remote servers, and can be compared over multiple runs. MLflow Tracking comes with an API and a web interface to easily observe all logged parameters and artifacts.


## Logging metrics & parameters

The main reason to use MLflow Tracking is to log and store parameters and metrics during a MLflow run. 

* *Parameters* represent the input parameters used for training, e.g. the initial learning rate. 
* *Metrics* are used to track the progress of the model training and are usually updated over the course of a model run. 
* *Tags* are further information that can be stored to identify the model, run, etc.

Parameters and metrics can be easily logged by calling `mlflow.log_param` and `mlflow.log_metric`. One can also specify a tag to identify the run by using `mlflow.set_tag`. Belows example show how to use each method within a run.

```python
run_name = "tracking-example-run"
experiment_name = "tracking-experiment"
mlflow.set_experiment(experiment_name)

with mlflow.start_run(run_name=run_name) as run:

    # Parameters
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_params({"epochs": 0.05, "final_activation": "sigmoid"})

    # Tags
    mlflow.set_tag("env", "dev")

    # Metrics
    mlflow.log_metric("loss", 0.001)
    mlflow.log_metrics({"acc": 0.92, "auc": 0.90})

    # It is possible to log a metrics series (for example a training history)
    for val_loss in [0.1, 0.01, 0.001, 0.00001]:
        mlflow.log_metric("val_loss", val_loss)

    run_id = run.info.run_id
    experiment_id = run.info.experiment_id
    print(f"run_id: {run_id}")
    print(f"experiment_id: {experiment_id}")
```


## Logging artifacts

*Artifacts* represent any kind of file to save during training, such as plots and model weights. It is possible to log such files as well, and place them within the same run as parameters and metrics. This means everything created within a ML run is saved at one point. Artifact files can be either single local files, or even full directories. The following example all the contents of a local directory as artifacts.

```python
# Create some files to preserve as artifacts
features = "rooms, zipcode, median_price, school_rating, transport"
data = {"state": "TX", "Available": 25, "Type": "Detached"}

# Create couple of artifact files under the directory "data"
os.makedirs("data", exist_ok=True)
with open("data/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
with open("data/features.txt", "w") as f:
    f.write(features)

# Write all files in "data" to root artifact_uri/states
with mlflow.start_run(run_id=run_id) as run:
    mlflow.log_artifacts("data", artifact_path="states")
    
    # get and print the URI where the artifacts have been logged to
    artifact_uri = mlflow.get_artifact_uri()
    print(f"run_id: {run.info.run_id}")
    print(f"Artifact uri: {artifact_uri}")
```

## Autolog

Previously, all the parameters, metrics, and files have been logged manually by the user. The *autolog*-feature of MLflow allows for automatic logging of metrics, parameters, and models without the need for an explicit log statements. This feature needs to be activated previous to the execution of a run by calling `MLflow.sklearn.autolog()`.

```python

mlflow.sklearn.autolog()

# Start an MLflow run with the specified run name 
# Create a ML model with the specified parameters 
# Fit the model using input data and target data

mlflow.sklearn.autolog(disable=True)
```

Even though this is a very convenient feature, it is a good practice to log metrics manually, as this gives more control over a ML run.
