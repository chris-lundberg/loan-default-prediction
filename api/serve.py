import lightgbm as lgb

from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel

ml_models = {}

model_file = "lgbm_model.txt"

@asynccontextmanager
async def lifespan(app: FastAPI):

    ml_models["loan_classifier"] = lgb.Booster(model_file=model_file)
    yield

    ml_models.clear()

app = FastAPI(lifespan=lifespan)

class LoanApplication(BaseModel):

    loan_amnt: float
    int_rate: float
    installment: float
    annual_inc: float
    dti: float
    open_acc: float
    pub_rec: float
    revol_bal: float
    revol_util: float
    total_acc: float
    mort_acc: float
    pub_rec_bankruptcies: float

class LendingDecision(BaseModel):

    result: float
    
@app.post("/predict/")
async def classify(features: LoanApplication) -> LendingDecision:

    features = list(features.model_dump().values())

    model_output = ml_models["loan_classifier"].predict([features])

    return {"result": model_output}