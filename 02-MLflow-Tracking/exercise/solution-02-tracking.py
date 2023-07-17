import os
# TODO: import mlflow
import mlflow


# -- Params
# TODO log a learning_rate of 0.01
mlflow.log_param("learning_rate", 0.01)

params = {"epochs": 0.05, "final_activation": "sigmoid"}
# TODO: log the above mentioned parameters to mlflow
mlflow.log_params(params)

# -- Tags
# TODO: set an environment tag to dev and a username tag to your name
mlflow.set_tags({"environment": "dev", "username": "sebastian-blum"})

# -- Metrics
# TODO: Log a F-score of 0.7
mlflow.log_metric("F-score", 0.7)

# TODO: log the following accuracies as metrics to your logistic-regression run
lr_run_id = "INSERT-RUN-ID"
accuracy_list = [0.6, 0.6, 0.8, 0.9]
with mlflow.start_run(run_id=lr_run_id):
    for val_acc in accuracy_list:
        mlflow.log_metric("val_acc", val_acc)

# -- Artifacts
# Create an example file output/test.txt
file_path = "outputs/test.txt"
if not os.path.exists("outputs"):
    os.makedirs("outputs")
with open(file_path, "w") as f:
    f.write("hello world!")

# TODO: store the previous created file in the data/subfolder subdirectory
mlflow.log_artifact(local_path=file_path, artifact_path="data/subfolder")

# TODO: get and print the URI where the artifacts have been logged to
artifact_uri = mlflow.get_artifact_uri()
print(artifact_uri)


# -- Autolog
import mlflow.sklearn
import numpy as np
from sklearn.ensemble import RandomForestRegressor

params = {"n_estimators": 4, "random_state": 42}

# TODO: start autologging the upcoming run
mlflow.sklearn.autolog()

run_name = 'autologging model example'
with mlflow.start_run(run_name=run_name) as run:
    rfr = RandomForestRegressor(**params).fit(np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), [1, 1, 1])
    print(f"run_id: {run.info.run_id}")

# TODO: stop autologging the upcoming run
mlflow.sklearn.autolog(disable=True)
