import time
import platform
from argparse import ArgumentParser
import mlflow
from mlflow.entities import Param,Metric,RunTag

mlflow.set_tracking_uri("http://127.0.0.1:5000/")
print("MLflow Version:", mlflow.__version__)
print("Tracking URI:", mlflow.tracking.get_tracking_uri())
client = mlflow.tracking.MlflowClient()

def run(alpha, run_origin):
    with mlflow.start_run(run_name=run_origin) as run:
        print("runId:",run.info.run_id)
        print("experiment_id:", run.info.experiment_id)
        print("experiment_name:", client.get_experiment(run.info.experiment_id).name)
        print("artifact_uri:", mlflow.get_artifact_uri())
        print("alpha:", alpha)
        print("run_origin:", run_origin)
        mlflow.log_param("alpha", alpha)
        mlflow.log_metric("rmse", 0.789)
        mlflow.set_tag("run_origin", run_origin)
        mlflow.set_tag("version.mlflow", mlflow.__version__)
        mlflow.set_tag("version.python", platform.python_version())
        mlflow.set_tag("version.platform", platform.system())
        with open("info.txt", "w") as f:
            f.write("Hi artifact")
        mlflow.log_artifact("info.txt")
        params = [ Param("p1","0.1"), Param("p2","0.2") ]
        now = round(time.time())
        metrics = [ Metric("m1",0.1,now,0), Metric("m2",0.2,now,0) ]
        tags = [ RunTag("tag1","hi1"), RunTag("tag2","hi2") ]
        client.log_batch(run.info.run_id, metrics, params, tags)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--experiment_name", dest="experiment_name", help="Experiment name", default="hello_world", type=str)
    parser.add_argument("--alpha", dest="alpha", help="alpha", default=0.1, type=float )
    parser.add_argument("--run_origin", dest="run_origin", help="run_origin", default="LocalRun")
    args = parser.parse_args()
    print("Arguments:")
    for arg in vars(args):
        print(f"  {arg}: {getattr(args, arg)}")
    if args.experiment_name is not None:
        mlflow.set_experiment(args.experiment_name)
    run(args.alpha,args.run_origin)
