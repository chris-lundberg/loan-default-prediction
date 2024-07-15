import lightgbm as lgb
from starlette.requests import Request
from ray import serve

@serve.deployment(num_replicas=2, ray_actor_options={"num_cpus": 0.2, "num_gpus": 0})
class LoanClassifier:
    def __init__(self, model_file: str="lgbm_model.txt"):
        # Load model
        self.model = lgb.Booster(model_file=model_file)

    def classify(self, features: list) -> str:
        # Run inference
        model_output = self.model.predict(features)

        return {"result": model_output}
    
    async def __call__(self, starlette_request: Request) -> dict:
        payload = await starlette_request.json()

        input_vector = list(payload.values())
        return self.classify([input_vector])

loan_default_app = LoanClassifier.bind()