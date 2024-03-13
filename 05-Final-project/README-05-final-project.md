# Final Project

There are two Projects to choose from. Only one is needed to pass the final exercise. Yet, of course you can do both if you are keen on doing so.

Extend the code with everything you know about MLflow now, meaning you track relevant metrics, parameters, further model information & artifacts, and register the model to the Mlflow Registry.
You can also choose to change the code as needed, meaning to calculare further metrics or intend blocks of code. It's up to you. The goal of this exercise is that you make yourself familiar with the MLflow API on a real ML example! Of course, you can choose `mlflow.autolog()` if you are lame and don't want to learn anything. ;)

## Keras | CNN

The first example implements a basic Keras Convolutional Neural Network on the MNIST dataset. The example can also be found on the official [keras documentation](https://keras.io/examples/vision/mnist_convnet/).

## Scikit | SVM

The second example implements a scikit based Support Vector Machine based on the breast cancer dataset. Its based on a [datacamp tutorial](https://www.datacamp.com/tutorial/svm-classification-scikit-learn-python), so if you are itnerested in it you can check it out of course.

## Bonus Exercise - Dataset

There is a [mlflow.data](https://mlflow.org/docs/2.10.2/python_api/mlflow.data.html) module which we didn't discuss yet. The Dataset API provides basic training data tracking capabilities. Try to write x_train, x_test, y_train and y_test data each to the Dataset API. If you managed to solve this task correctly, these datasets should show up in the GUI of a run under the "Datasets" section.

Note that this feature does not store any data itself but only metadata about datasets such as "including the name, digest (hash), schema, and profile of the dataset as well as source information (e.g. the S3 bucket)".

Hint: You need to go to the linked documentation page to find the appropriate function to cast the data into an object that can be read by the dataset API.

## Bonus Exercise - Serving

For all of you that got through this exercise at ease, try to *serve* your model with the `mlflow models serve` command. The goal is to have some API endpoint running which allows to run predictions on your model. The server could be tested for example by using `curl`, `wget` in command line or `requests` Python library.

For explanation how serving works, you can refer to our presentation or check the [documentation](https://mlflow.org/docs/2.10.2/cli.html#mlflow-models-serve).
