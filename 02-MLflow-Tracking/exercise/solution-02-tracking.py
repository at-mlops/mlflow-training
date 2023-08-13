import os

# TODO: import mlflow
import mlflow

# TODO: Set the tracking URI to your localhost ip http://127.0.0.1:PORT/
# (PORT is usually 5000)
mlflow.set_tracking_uri("http://127.0.0.1:5008")

# TODO: Start a new mlflow run "mlflow-tracking" and export its run_id
# IMPORTANT: Keep the naming of "exercise_2_id", and "tracking_run_id" as they are needed later
exercise_2_id = mlflow.set_experiment("exercise-02").experiment_id
tracking_run_id = mlflow.start_run(run_name="mlflow-tracking").info.run_id

# -- Params
# TODO log a learning_rate of 0.01
mlflow.log_param("learning_rate", 0.01)

params = {"epochs": 0.05, "final_activation": "sigmoid"}
# TODO: log the above mentioned parameters to mlflow
mlflow.log_params(params)

# -- Tags
# TODO: set an "environment" tag to "dev" and a "username" tag to "your name"
mlflow.set_tags({"environment": "dev", "username": "sebastian-blum"})

# -- Metrics
# TODO: Log a F-score of 0.7
mlflow.log_metric("F-score", 0.7)


mlflow.end_run()  # end the previous run to be able to start a new one

# TODO: log the following accuracies as metrics to your logistic-regression run from the previous experiment
# "exercise-01.1-YOUR-NAME" with its run_id and experiment_id. HINT: Look also in the web UI
lr_run_id = "58ac5e583fc14d5abeb560f91823f719"
experiment_id = "726848279522163129"
mlflow.set_experiment(experiment_id=experiment_id)
accuracy_list = [0.6, 0.6, 0.8, 0.9]
with mlflow.start_run(run_id=lr_run_id):
    for val_acc in accuracy_list:
        mlflow.log_metric("val_acc", val_acc)

# -- Artifacts
mlflow.set_experiment(experiment_id=exercise_2_id)
mlflow.start_run(run_id=tracking_run_id)

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
print(f"Artifact_uri: {artifact_uri}")

# End previous runs
mlflow.end_run()


# -- Autolog
import mlflow.sklearn
import numpy as np
from sklearn.ensemble import RandomForestRegressor

params = {"n_estimators": 4, "random_state": 42}

# TODO: start autologging the upcoming run
mlflow.sklearn.autolog()

run_name = "autologging model example"
with mlflow.start_run(run_name=run_name) as run:
    rfr = RandomForestRegressor(**params).fit(
        np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), [1, 1, 1]
    )
    print(f"run_id: {run.info.run_id}")

# TODO: stop autologging
mlflow.sklearn.autolog(disable=True)
