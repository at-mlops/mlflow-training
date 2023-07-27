import mlflow

# TODO: Set the tracking URI to your http://127.0.0.1:PORT/
# (PORT is usually 5000)
mlflow.set_tracking_uri("http://127.0.0.1:5008/")

# TODO: Set your name and create a MLflow experiment
experiment_name = "exercise-01.1-sebastian-blum"
mlflow.set_experiment(experiment_name)

# Create two mlflow runs with different names within the previously created mlflow experiment
# The first on is called: "logistic-regression"
# The second one is called "support-vector-machine"
run_name_lr = "logistic-regression"
run_name_svm = "support-vector-machines"

# TODO: start your MLflow run for run_name_lr
mlflow.start_run(run_name=run_name_lr)

# TODO set the run to active and export it to the variable "run_lr"
run_lr = mlflow.active_run()

print(f"Active run_id: {run_lr.info.run_id}")

# TODO: end your MLflow run
mlflow.end_run()

# TODO: Now repeat the above steps to create the same for run_name_svm
# export the active run to run_svm
mlflow.start_run(run_name=run_name_svm)
run_svm = mlflow.active_run()
print(f"Active run_id: {run_svm.info.run_id}")
mlflow.end_run()

# TODO: Set the experiment as active and export its experiment_id
experiment_name = "exercise-01.2-context-manager"
mlflow_experiment_id = mlflow.set_experiment(experiment_name).experiment_id
print(f"Experiment_id: {mlflow_experiment_id}")

run_name = "context-manager-run"
# TODO: run the mlflow run using the context manager. Export its run id as run_id
with mlflow.start_run(run_name=run_name) as run:
    run_id = run.info.run_id
    print(f"Active run_id: {run_id}")
