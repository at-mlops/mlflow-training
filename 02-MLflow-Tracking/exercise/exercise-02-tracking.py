import os

# TODO: import mlflow
# ???

# TODO: Set the tracking URI to your localhost ip http://127.0.0.1:PORT/
# (PORT is usually 5000)
# ???

exercise_2_id = mlflow.set_experiment("exercise-02").experiment_id
tracking_run_id = mlflow.start_run(run_name="mlflow-tracking").info.run_id

# -- Params
# TODO log a learning_rate of 0.01
# ???


params = {"epochs": 0.05, "final_activation": "sigmoid"}
# TODO: log the above mentioned parameters to mlflow
# ???

# -- Tags
# TODO: set an environment tag to dev and a username tag to your name
# ???

# -- Metrics
# TODO: Log a F-score of 0.7
# ???


mlflow.end_run()  # end the previous run to be able to start a new one

# TODO: log the following accuracies as metrics to your logistic-regression run from the previous experiment
# "introduction-set-experiment" with its run_id and experiment_id
lr_run_id = "INSERT-RUN-ID"
experiment_id = "INSERT-EXPERIMENT-ID"
accuracy_list = [0.6, 0.6, 0.8, 0.9]
# ???


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
# ???

# TODO: get and print the URI where the artifacts have been logged to
# ???

# End previous runs
mlflow.end_run()


# -- Autolog
import mlflow.sklearn
import numpy as np
from sklearn.ensemble import RandomForestRegressor

params = {"n_estimators": 4, "random_state": 42}

# TODO: start autologging the upcoming run
# ???

run_name = "autologging model example"
with mlflow.start_run(run_name=run_name) as run:
    rfr = RandomForestRegressor(**params).fit(
        np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), [1, 1, 1]
    )
    print(f"run_id: {run.info.run_id}")

# TODO: stop autologging
# ???
