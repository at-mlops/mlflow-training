# Final Project

Extend the code with everything you know about MLflow now, meaning you track relevant metrics, parameters, further model information & artifacts, and register the model to the Mlflow Registry. Try to train minimum 3 different model architectures or hyperparameter sets to be able to compare your models and choose the best one. If you want to add more python modules you can do so by adding files to `src/mlflow_training` the project is setup so that you can import code from there. 

```
from mlflow_training.test_env import RandomForestRegressor
```

You can also choose to change the code as needed, meaning to calculate further metrics or intend blocks of code. It's up to you. The goal of this exercise is that you make yourself familiar with the MLflow API on a real ML example! Of course, you can choose `mlflow.autolog()` if you are lame and don't want to learn anything. ;)

## Dataset 

The example implements a scikit based Support Vector Machine based on the breast cancer dataset. Its based on a [datacamp tutorial](https://www.datacamp.com/tutorial/svm-classification-scikit-learn-python), so if you are interested in it you can check it out of course.

## Bonus Exercise - Serving

For all of you that got through this exercise at ease, try to *serve* your model with the `mlflow models serve` command. The goal is to have some API endpoint running which allows to run predictions on your model.

For explanation how serving works, you can refer to our presentation or check the [documentation](https://mlflow.org/docs/2.10.2/cli.html#mlflow-models-serve).

You can test your model endpoint and send requests to your model in the notebook `test_model_endpoint.ipynb`
