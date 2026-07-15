from fastapi import FastAPI
from backend.parser import get_pkmn
from backend.parser import get_Usage
from backend.parser import get_usage_ranking
from backend.parser import get_all_pokemon
app=FastAPI()
@app.get("/")
def home():
    return {
        "message": "Pokemon_Guide website is working"
    }
@app.get("/pokemon/{name}")
def pokemon(name:str):
    pokemon=get_pkmn(name)
    if pokemon is None:
        return {
            "Error": "Pokemon not found"
        }
    return pokemon
@app.get("/{name}/Usage")
def Usage(name: str):
    Usage_rate=get_Usage(name)
    return Usage_rate
@app.get("/home")
def top_20_usage():
    return get_usage_ranking()
@app.get("/Pokemon")
def get_all():
    return get_all_pokemon()