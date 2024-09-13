from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router  import router
import store
from database import engine

store.Base.metadata.create_all(bind= engine)

app = FastAPI()

origin = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origin,
    allow_credentials= True,
    allow_methods = ["*"],
    allow_headers= ["*"],
)

app.include_router(router)

@app.get("/")
def root():
    return {"Message": "API Working."}

