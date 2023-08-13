# Important: The MLflow webserver needs to run so the API can log to the server. Otherwise it doesn't work.
# PLEASE RUN THE THE MLFLOW UI USING 'mlflow ui'

# TODO: Import the MLflow package
# ???

# TODO: Set the tracking URI to your localhost ip http://127.0.0.1:PORT/
# (PORT is usually 5000)
# ???

# TODO: Set your name and create and set an MLflow experiment
experiment_name = "exercise-01.1-YOUR-NAME"
# ???


# Create two mlflow runs with different names within the previously created mlflow experiment
# The first on is called: "logistic-regression"
# The second one is called "support-vector-machine"
run_name_lr="logistic-regression"
run_name_svm="support-vector-machines"

# TODO: start your MLflow run for run_name_lr
# ???


# TODO  Export the active run ID to the variable "run_lr"
# ???

print(f"Active run_id for 'run_name_lr': {run_lr.info.run_id}")

# TODO: end your MLflow run
# ???


# TODO: Now repeat the above steps to create the same for run_name_svm
# export the active run to run_svm
# ???


# TODO: Set the experiment as active and export its experiment_id as "mlflow_experiment_id"
experiment_name = "exercise-01.2-context-manager"
# ???
print(f"Experiment_id for 'exercise-01.2-context-manager': {mlflow_experiment_id}")

run_name = "context-manager-run"
# TODO: run the mlflow run using the context manager. Export its run id as run_id
# ???
    print(f"Active run_id for 'context-manager-run': {run_id}")
