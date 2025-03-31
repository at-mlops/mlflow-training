# LLM-Tracing 

MLflow Tracing is a feature that enhances LLM observability in your Generative AI (GenAI) applications by capturing detailed information about the execution of your application's services. Tracing provides a way to record the inputs, outputs, and metadata associated with each intermediate step of a request, enabling you to easily pinpoint the source of bugs and unexpected behaviors.

You can enable Tracing with different mlflow flavors for the most used frameworks. For example: 

```python 
mlflow.openai.autolog()

# or 

mlflow.langchain.autolog()
```

# Log the Agent 

There are multiple ways to Log a Chain or Agent in MLFlow. 

### Pyfunc
https://mlflow.org/docs/latest/api_reference/python_api/mlflow.pyfunc.html#mlflow.pyfunc.log_model 

### Langchain Flavor
https://mlflow.org/docs/latest/llms/langchain/notebooks/langchain-quickstart#logging-the-chain-in-mlflow

```python 
model_input = {
    "query": "Who is the current chancellor of Germany? April 2025",
    "session_id": str(uuid4())
}

signature = infer_signature(model_input, "The chancellor of Germany is Olaf Scholz")

with mlflow.start_run() as run:
    mlflow.pyfunc.log_model(
        artifact_path="langgraph_model",
        python_model=LangGraphWrapper(system_message=SYSTEM_MESSAGE, tools=[wikipedia_tool]),
        signature=signature,
        registered_model_name="MyLanggraphAgent"
    )
    mlflow.log_param("system_message", SYSTEM_MESSAGE)
    mlflow.log_param("tools", [wikipedia_tool.name])
    
run_id = run.info.run_id
```