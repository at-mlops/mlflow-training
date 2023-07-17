import os
# TODO: import mlflow
???


# -- Params
# TODO log a learning_rate of 0.01
???

params = {"epochs": 0.05, "final_activation": "sigmoid"}
# TODO: log the above mentioned parameters to mlflow
???

# -- Tags
# TODO: set an environment tag to dev and a username tag to your name
???

# -- Metrics
# TODO: Log a F-score of 0.7
???

# TODO: log the following accuracies as metrics to your previously created "logistic-regression" run
lr_run_id = "INSERT-RUN-ID"
accuracy_list = [0.6, 0.6, 0.8, 0.9]
???


# -- Artifacts
# Create an example file output/test.txt
file_path = "outputs/test.txt"
if not os.path.exists("outputs"):
    os.makedirs("outputs")
with open(file_path, "w") as f:
    f.write("hello world!")

# TODO: store the previous created file in the data/subfolder subdirectory
???

# TODO: get and print the URI where the artifacts have been logged to
???



# -- Autolog
import mlflow.sklearn
import numpy as np
from sklearn.ensemble import RandomForestRegressor

params = {"n_estimators": 4, "random_state": 42}

# TODO: start autologging the upcoming run
???

run_name = 'autologging model example'
with mlflow.start_run(run_name=run_name) as run:
    rfr = RandomForestRegressor(**params).fit(np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), [1, 1, 1])
    print(f"run_id: {run.info.run_id}")

# TODO: stop autologging
???

