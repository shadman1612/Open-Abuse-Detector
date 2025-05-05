from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
classifier = pipeline("text-classification", model="unitary/toxic-bert")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Tweet(BaseModel):
    text: str

@app.post("/classify")
def classify(tweet: Tweet):
    result = classifier(tweet.text)[0]
    return {"label": result['label'], "score": result['score']}
