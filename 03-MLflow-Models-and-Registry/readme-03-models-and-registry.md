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

The MLflow Model Registry provides a central model store to manage the lifecycle of an ML Model. This allows to register MLflow models like the *RandomForestRegressor* from the previous section to the Model Registry and include model versioning, tags and alias.

To register a model you can either use the mlflow function `mlflow.register_model` or include the `registered_model_name` in the function `log_model`. You can also add a schema for your model if you add the `signature` attribute.  

https://mlflow.org/docs/latest/model-registry.html 

```python
import mlflow.sklearn
from mlflow.models import infer_signature
from sklearn.ensemble import RandomForestRegressor

run_name = "registry-example-run"
params = {"n_estimators": 4,
          "random_state": 42}

model_name = "RandomForestRegressionModel"
run_name = 'model registry example'
with mlflow.start_run(run_name=run_name) as run:
    rfr = RandomForestRegressor(**params).fit([[0, 1, 0]], [1])

    X = [[0, 1, 0]]
    y_hat = rfr.predict(X)
    signature = infer_signature(X, y)

    mlflow.log_params(params)
    # Log and store the model and the MLflow Model Registry
    mlflow.sklearn.log_model(
        rfr,
        artifact_path="sklearn-model",
        registered_model_name=model_name, #Optional
        signature=signature, #Optional
    )
```

Once registered to the model registry the model is versioned. This enables to load a model based on a specific version and to change a model version respectively. Registered models can then be annotated with tags and aliases.

```python
# Load model for prediction. Keep note that we now specified the model version.
model_version = 1

model = mlflow.sklearn.load_model(
    model_uri=f"models:/{model_name}/{model_version}", dst_path="models/"
)

# Predict based on the loaded model
data = [[0, 1, 0]]
y_hat = model.predict(data)
print(f"predictions: {y_hat}")
```

Let's add an alias to our registered model next. (You can also add aliases and descriptions to your model via the ui)

```python
from mlflow.client import MLflowClient 
from pprint import pprint

client = MlflowClient()

# Add alias to model.
# The set_registered_model_alias() method identifies a model
# by its name and version which we can obtain from the ModelVersion object "mv".
client.set_registered_model_alias(
    name = model_name,
    alias = "myalias",
    version = model_version)

# print registered models
for rm in client.search_registered_models():
    pprint(dict(rm), indent=4)
```

> **_NOTE:_**  Above example uses the mlflow.client module. It provides a lower level API that directly translates to MLflow REST API calls for similar features of Experiments, Runs, Model Versions, and Registered Models


