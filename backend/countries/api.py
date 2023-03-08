# backend/countries/api.py
from fastapi import APIRouter
from pydantic import BaseModel
from firebase_admin import credentials, initialize_app, firestore, get_app

cred = credentials.Certificate("./.venv/firebase.json")
app = initialize_app(cred, name="nomad")
db = firestore.client()

countries = APIRouter()


class Country(BaseModel):
    id: str


@countries.post("/countries")
async def create(country: Country):
    db.collection("countries").add(country.dict())
    return country


@countries.get("/countries")
async def read():
    countries = db.collection("countries").stream()
    return [country.to_dict() for country in countries]


@countries.put("/countries/{id}")
async def update(id: str, country: Country):
    db.collection("countries").document(id).set(country.dict())
    return country


@countries.delete("/countries/{id}")
async def delete(id: str):
    db.collection("countries").document(id).delete()
    return {"message": "Country deleted successfully."}
