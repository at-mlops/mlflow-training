
# Import the sklearn models from MLflow
import mlflow.sklearn
import mlflow
from pprint import pprint
from sklearn.ensemble import RandomForestRegressor

mlflow.set_tracking_uri("http://127.0.0.1:5000/")
# FIXME: if not set, it will log to a local file, instead of the remote tracking server.

run_name = "mlflow-models-and-registry"
experiment_name = "mlflow-models-and-registry"
mlflow.set_experiment(experiment_name)

# -- MLflow Models

# log model to current run
with mlflow.start_run(run_name=run_name) as run:
    params = {"n_estimators": 4, "random_state": 42}
    rfr = RandomForestRegressor(**params).fit([[0, 1, 0]], [1])
    mlflow.log_params(params)
    # TODO: Log the model rfr and give it the path "sklearn-model"
    ???

    # TODO: modify the model_uri to load from the path "sklearn-model"
    model_uri = f"{???}:/{run.info.run_id}/{???}"

# TODO: Load the model using the model uri to test it
???

data = [[0, 1, 0]]
model_pred = model.predict(data)
print(f"model_pred: {model_pred}")



# -- MLflow Model Registry

model_name = "sklearn-model-name"
# register model in mlflow registry
# TODO: Register the model to the model registry using the model_uri from before and the model_name
mv = ???
print("Name: {}".format(mv.name))
print("Version: {}".format(mv.version))
print("Stage: {}".format(mv.current_stage))



# TODO: modify the model_uri to load the model from the registry
model_uri = f"{???}:/{???}/{mv.version}"
model = mlflow.sklearn.load_model(model_uri=model_uri)

data = [[0, 1, 0]]
model_pred = model.predict(data)
print(f"model_pred: {model_pred}")


# Transition the model to another stage
# from mlflow import MLflowClient 
from mlflow.client import MlflowClient # FIXME: had to import it from mlflow.client
client = MlflowClient()

# TODO: Transition the model to the stage "Production"
stage = ???  # None, Staging, Production

client.transition_model_version_stage(
    name=model_name,
    version=mv.version,
    ???
)

# print registered models
for rm in client.search_registered_models():
    pprint(dict(rm), indent=4)
