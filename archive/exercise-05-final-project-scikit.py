
# Import the sklearn models from MLflow
import mlflow.sklearn
import mlflow.pyfunc
from sklearn.ensemble import RandomForestRegressor

run_name = "models-example-run"

with mlflow.start_run(run_name=run_name) as run:
    params = {"n_estimators": 4, "random_state": 42}
    # TODO dev: new model (SVM)
    rfr = RandomForestRegressor(**params).fit([[0, 1, 0]], [1])
    mlflow.log_params(params)

    # TODO dev: calculate metrics

    # create accuracy image
# TODO: modify the model_uri so it gets the name of your model "YOUR-NAME-sklearn-rfr"
model_uri = f"runs:/{run.info.run_id}/{}"
print(f"model_uri: {model_uri}")




model = mlflow.pyfunc.load_model(model_uri=model_uri)
data = [[0, 1, 0]]
model_pred = model.predict(data)
print(f"model_pred: {model_pred}")
