# MLflow Overview


0. Welcome and Introduction Rounds
1. What is MLflow? Why do we use it?
   1. Relate to ML Lifecycle
   2. What are MLFlows main functionalities? (Short overview)
      1. Theory MLflow
         1. MLflow Tracking
         2. MLflow Models
         3. MLflow Model Registry
         4. MLflow Projects
      2. Theory Experiments & Runs
      3. Hands-On
         1. Set up MLflow Experiment & Run


## What is MLflow? Why do we use it?

* Tracking ML model development
* Versioning Models
* Model Registry
* Comes with own API in different languages (R, Python, Java)

### Theory MLflow

* MLflow Tracking
  * Store model parameters
  * Store model metrics
  * Store models
  * Store images and other artifacts
  * autolog
  * Display & View metrics
    * Compare models, runs, and experiments
* MLflow Models & Model Registry
  * allows unified model format
    * so called flavor
  * register models
  * load models
  * version models
  * stage models
* MLflow Projects
  * store full ml code as unified project as 
### Theory Experiments & Runs

```python
import mlflow

# mlflow.set_tracking_uri("http://127.0.0.1:5000/")

experiment_name = "introduction-create-experiment"
mlflow.create_experiment(experiment_name)

mlflow.start_run()
run = mlflow.active_run()
print(f"Active run_id: {run.info.run_id}")
mlflow.end_run()


experiment_name = "introduction-set-experiment"
mlflow.set_experiment(experiment_name)

run_name = "context-manager-run"
with mlflow.start_run(run_name=run_name) as run:
    run_id = run.info.run_id
    print(f"Active run_id: {run_id}")

## Nested runs

# Create child runs based on the run ID
with mlflow.start_run(run_id=run_id) as parent_run:
    print("parent run_id: {}".format(parent_run.info.run_id))
    with mlflow.start_run(nested=True, run_name="test_dataset_abc") as child_run:
        mlflow.log_metric("acc", 0.91)
        print("child run_id : {}".format(child_run.info.run_id))

with mlflow.start_run(run_id=run_id) as parent_run:
    print("parent run_id: {}".format(parent_run.info.run_id))
    with mlflow.start_run(nested=True, run_name="test_dataset_xyz") as child_run:
        mlflow.log_metric("acc", 0.90)
        print("child run_id : {}".format(child_run.info.run_id))
```

### Hands-On Experiments

see [here](01-MLflow-Overview/01-overview.py)