# MLflow Overview

The following gives an overview on how to set up experiments and runs in general, and gives an example on how to work with the MLflow API in general. Let's begin by importing it.

```python
import mlflow
```

## Tracking URI

Before we begin, we need to configure MLflow to log to a remote, or local, tracking server. This allows to manage results on in a central place and share them across a team. To get access to a tracking server it is needed to set a MLflow tracking URI. This can be done multiple way. Either by setting an environment variable `MLFLOW_TRACKING_URI` to the servers URI, or by adding it to the start of our code. We will do it manually here

```python
# Log to localhost on PORT 5000
mlflow.set_tracking_uri("http://127.0.0.1:5000/")
```

## Mlflow experiments

MLflow experiments are a part of MLflow’s tracking component that allow to group runs together based on custom criteria. For example multiple model runs with different model architectures might be grouped within one experiment to make it easier for evaluation.

```python
experiment_name = "introduction-experiment"

# Create and experiment
mlflow.create_experiment(experiment_name)

# Set an experiment, creates if none exists
mlflow.set_experiment(experiment_name)
```

## Mlflow run

An MLflow run is an execution environment for a piece of machine learning code. Whenever parameters or performances of a ML run or experiment should be tracked, a new MLflow run is created. This is easily done using `MLflow.start_run()`. Using `MLflow.end_run()` the run will similarly be ended.

```python
run_name = "example-run"

mlflow.start_run()
run = mlflow.active_run()
print(f"Active run_id: {run.info.run_id}")
mlflow.end_run()
```

It is a good practice to pass a run name to the MLflow run to identify it easily afterwards. It is also possible to use the context manager as shown below, which allows for a smoother style.

```python
run_name = "context-manager-run"

with mlflow.start_run(run_name=run_name) as run:
    run_id = run.info.run_id
    print(f"Active run_id: {run_id}")
```

**Child runs**
It is possible to create child runs of the current run based on the run ID. This can be used for example to gain a better overview of multiple run. Belows code shows how to create a child run.

```python
# Create child runs based on the run ID
with mlflow.start_run(run_id=run_id) as parent_run:
    print("parent run_id: {}".format(parent_run.info.run_id))
    with mlflow.start_run(nested=True, run_name="test_nested_run_abc") as child_run:
        mlflow.log_metric("acc", 0.91)
        print("child run_id : {}".format(child_run.info.run_id))

with mlflow.start_run(run_id=run_id) as parent_run:
    print("parent run_id: {}".format(parent_run.info.run_id))
    with mlflow.start_run(nested=True, run_name="test_nested_run_xyz") as child_run:
        mlflow.log_metric("acc", 0.90)
        print("child run_id : {}".format(child_run.info.run_id))
```
