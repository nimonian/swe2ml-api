from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.models.Rudiment import Rudiment

app = FastAPI()

origins = ["http://localhost", "http://localhost:5173", "https://swe2ml.netlify.app/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
def pong():
    return {"message": "pong"}


@app.get("/rudiments/{rudiment_id}")
def get_rudiment(rudiment_id: str) -> Rudiment:
    try:
        rudiment = Rudiment.create(rudiment_id)
        return rudiment
    except ValueError as e:
        print(e)
        raise HTTPException(status_code=400, detail="Rudiment not found.")
