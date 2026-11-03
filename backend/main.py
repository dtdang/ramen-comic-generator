
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Ramen Buddy Comic API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://dtdang.github.io"
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

@app.get("/")
def home():
    return {"status": "online", "app": "Ramen Buddy"}

@app.get("/health")
def health():
    return {"status": "ok"}
