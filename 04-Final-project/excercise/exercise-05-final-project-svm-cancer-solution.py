# Import scikit-learn dataset library
# %%

import mlflow
from mlflow.models import infer_signature
import json
from tempfile import TemporaryDirectory
from pathlib import Path

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.pipeline import Pipeline


# %%


def train(model: Pipeline, model_name: str, params: dict):
    # Load dataset
    print("Loading data...")
    cancer = datasets.load_breast_cancer()

    experiment = mlflow.set_experiment("final-project")
    with mlflow.start_run(experiment_id=experiment.experiment_id) as run:
        ## Model training

        # log config
        with TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "dataset.json"
            dataset_config = {
                "features": list(cancer.feature_names),
                "target": list(cancer.target_names),
            }
            with file_path.open("w") as outfile:
                json.dump(dataset_config, outfile)

            mlflow.log_artifact(file_path)

        mlflow.log_params(params)

        # Split dataset into training set and test set; 70% training and 30% test
        X_train, X_test, y_train, y_test = train_test_split(
            cancer.data, cancer.target, test_size=0.3, random_state=109
        )

        # Create a svm Classifier
        clf = model(**params)

        # Train the model using the training sets
        print("Model training...")
        clf.fit(X_train, y_train)

        # Predict the response for test dataset
        print("Model evaluation...")
        y_pred = clf.predict(X_test)
        signature = infer_signature(X_test, y_pred)

        accuracy = metrics.accuracy_score(y_test, y_pred)
        precision = metrics.precision_score(y_test, y_pred)
        recall = metrics.recall_score(y_test, y_pred)

        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.sklearn.log_model(
            clf,
            artifact_path="sklearn-model",
            registered_model_name=model_name,
            signature=signature,
        )

        return clf


if __name__ == "__main__":
    from sklearn.ensemble import RandomForestClassifier

    model = RandomForestClassifier
    params = {"n_estimators": 10, "max_depth": 5}

    clf = train(model=model, model_name="RandomForestFinalProject", params=params)
    print(clf)
