# MLflow Models

MLflow Models enables to manage and deploy machine learning models from multiple libraries. It allows to package your own ML model for later use in downstream tasks, e.g. real-time serving through a REST API. The package format defines a convention that saves the model in different *“flavors”* that can be interpreted by different downstream tools. Have a look at all the [possibilities](https://mlflow.org/docs/latest/python_api/index.html)


```python
# Import the sklearn models from MLflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor

run_name = "models-example-run"
params = {"n_estimators": 4, "random_state": 42}

# Start an MLflow run, train the RandomForestRegressor example model, and
# log its parameeters. In the end the model itself is logged and stored in MLflow
run_name = 'Model example'
with mlflow.start_run(run_name=run_name) as run:
    rfr = RandomForestRegressor(**params).fit([[0, 1, 0]], [1])
    mlflow.log_params(params)
    mlflow.sklearn.log_model(rfr, artifact_path="sklearn-model")

model_uri = "runs:/{}/sklearn-model".format(run.info.run_id)
model_name = f"RandomForestRegressionModel"

print(f"model_uri: {model_uri}")
print(f"model_name: {model_name}")
```

Once a model is stored in the correct format it can be identified by its `model_uri`, loaded, and used for prediction.

```python
# Load the model and use it for predictions
model = mlflow.sklearn.load_model(model_uri=model_uri)
data = [[0, 1, 0]]
model_pred = model.predict(data)
print(f"model_pred: {model_pred}")
```


# MLflow Registry

The MLflow Model Registry provides a central model store to manage the lifecycle of an ML Model. This allows to register MLflow models like the *RandomForestRegressor* from the previous section to the Model Registry and include model versioning, stage transitions, and annotations. In fact, by running `MLflow.sklearn.log_model` we already did exactly that. Look at how easy the MLflow API is to use. Let's have a look at the code again.

```python
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor

run_name = "registry-example-run"
params = {"n_estimators": 4,
          "random_state": 42}

run_name = 'model registry example'
with mlflow.start_run(run_name=run_name) as run:
    rfr = RandomForestRegressor(**params).fit([[0, 1, 0]], [1])
    mlflow.log_params(params)
    # Log and store the model and the MLflow Model Registry
    mlflow.sklearn.log_model(rfr, artifact_path="sklearn-model")

model_uri = f"runs:/{run.info.run_id}/sklearn-model"
model_name = f"RandomForestRegressionModel"

model = mlflow.sklearn.load_model(model_uri=model_uri)
data = [[0, 1, 0]]
model_pred = model.predict(data)
print(f"model_pred: {model_pred}")
```

Yet, it is also possible to register the MLflow model in the model registry by calling `MLflow.register_model` such as show in belows example.

```python
# The previously stated Model URI and name are needed to register a MLflow Model
mv = mlflow.register_model(model_uri, model_name)
print("Name: {}".format(mv.name))
print("Version: {}".format(mv.version))
print("Stage: {}".format(mv.current_stage))
```

Once registered to the model registry the model is versioned. This enables to load a model based on a specific version and to change a model version respectively. A registered model can be also modified to transition to another version or stage. Both use cases are shown in the example below.

```python
# Load model for prediction. Keep note that we now specified the model version.
model = mlflow.sklearn.load_model(
    model_uri=f"models:/{model_name}/{mv.version}"
)

# Predict based on the loaded model
data = [[0, 1, 0]]
model_pred = model.predict(data)
print(f"model_pred: {model_pred}")
```

Let's stage a model to `'Staging'`. The for-loop below prints all registered models and shows that there is indeed a model with a `'Staging'`-stage.

```python
# Transition the model to another stage
from mlflow.client import MLflowClient 
from pprint import pprint

client = MlflowClient()

stage = 'Staging'  # None, Production

client.transition_model_version_stage(
    name=model_name,
    version=mv.version,
    stage=stage
)

# print registered models
for rm in client.search_registered_models():
    pprint(dict(rm), indent=4)
```

> **_NOTE:_**  Above example uses the mlflow.client module. It provides a lower level API that directly translates to MLflow REST API calls for similar features of Experiments, Runs, Model Versions, and Registered Models


