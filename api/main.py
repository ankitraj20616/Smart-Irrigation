from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origin = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origin,
    allow_credentials= True,
    allow_methods = ["*"],
    allow_headers= ["*"],
)

@app.get("/")
def root():
    return {"Message": "API Working."}

