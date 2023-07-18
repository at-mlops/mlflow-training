# TODO: Import the MLflow package
# ???

# TODO: Set the tracking URI to your localhost ip http://127.0.0.1:PORT/ 
# (PORT is usually 5000)
# ???

# TODO: Set your name and create a MLflow experiment
experiment_name = "MLflow-training-YOUR-NAME"
# ???


# Create two mlflow runs with different names within the previously created mlflow experiment
# The first on is called: "logistic-regression"
# The second one is called "support-vector-machine"
run_name_lr="logistic-regression"
run_name_svm="support-vector-machines"

# TODO: start your MLflow run for run_name_lr
# ???


# TODO set the run to active and export it to the variable "run_lr"
# ???

print(f"Active run_id: {run_lr.info.run_id}")

# TODO: end your MLflow run
# ???


# TODO: Now repeat the above steps to create the same for run_name_svm
# export the active run to run_svm
# ???


# TODO: Set the experiment as active and export its experiment_id
experiment_name = "introduction-set-experiment"
# ???

run_name = "context-manager-run"
# TODO: run the mlflow run using the context manager. Export its run id as run_id
# ???
    print(f"Active run_id: {run_id}")
