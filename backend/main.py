# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from passports.api import passports
from countries.api import countries

from firebase_admin import credentials, initialize_app, firestore

cred = credentials.Certificate("./.venv/firebase.json")
app = initialize_app(credentials=cred, name="nomad")
db = firestore.client()

app = FastAPI()
app.include_router(passports, prefix="", tags=["passports"])
app.include_router(countries, prefix="", tags=["countries"])


# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello Nomads!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app')