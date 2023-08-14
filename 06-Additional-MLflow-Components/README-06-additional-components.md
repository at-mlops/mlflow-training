# Additional Components

Congratulations, you should know by now the fundamentals of MLflow and its main functionality. However, MLFlow is constantly in development and also offers a variety of other tools, some that just have been released.

## MLflow Serving (part of MLflow Models)

[MLFlow Serving](https://mlflow.org/docs/latest/models.html#mlflow-serving) is a component of the MLFlow platform designed to streamline the deployment and serving of machine learning models. It aims for an easy integration with various deployment frameworks and cloud platforms by easily serving models as RESTful API endpoints. This makes it straightforward to make predictions or inference calls from different applications and services to your MLflow Models.

For instance, you can deploy a trained image classification model and expose it as an API endpoint to classify images on-the-fly. MLFlow Serving offers versioning, scalability, and monitoring features, making it a seamless transition from development to deployment.

```bash
# serve local directory
mlflow models serve -m my_directory_to_model 

# or serve from model registry
mlflow models serve --model-uri runs:/<run-id>/model --no-conda
```


## MLflow Recipes  (from v2.3.2)

[MLFlow Recipes](https://mlflow.org/docs/latest/recipes.html) streamlines the creation and sharing of data preprocessing and transformation workflows. It allows data scientists and engineers to encapsulate common data preparation tasks into reusable and customizable "recipes." For example, you can create a recipe that performs data normalization and apply it to different datasets. These recipes can range from data cleaning and feature engineering to more complex data transformations and even training & tuning models. 
It is previously known as MLflow Pipelines and has already been released as experimental from version 1.27.0 to 2.2.2.

A detailed description can be found in this repository at [MLflow Recipes](./MLflow-Recipes.md)


## MLflow LLM Tracking (Large Language Models) (from v2.3.2)

[MLflow LLM Tracking](https://mlflow.org/docs/latest/llm-tracking.html) is an extension of the MLFlow platform specifically designed to facilitate the management and tracking of large language models, such as those based on the GPT (Generative Pre-trained Transformer) architecture. The Mlflow LLM Tracking component consists of two elements for logging and viewing the behavior of LLM’s. Firstly it is a set of APIs that allow for logging inputs, outputs, and prompts submitted and returned from LLM’s. Accompanying these APIs is a UI components that provides a simplified means of viewing the results of experimental submissions (prompts and inputs) and the results (LLM outputs).


## MLflow AI Gateway (from v2.5.0 experimental)

The MLflow AI Gateway service streamlines the utilization and oversight of various large language model (LLM) providers, like OpenAI and Anthropic, within organizations by offering a user-friendly interface for managing LLM-related requests through a unified endpoint. 
It enhances security by centrally managing API keys, mitigating risks associated with key exposure. Its flexibility also allows easy adaptation and management of routes for different LLM providers, facilitating the integration of new providers without altering gateway-interfacing applications. 