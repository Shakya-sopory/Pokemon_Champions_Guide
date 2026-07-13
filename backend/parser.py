import json
with open("data/gen9championsvgc2026regmb-1760.json","r",encoding="utf-8"
          )as f: 
    data=json.load(f)
pkmn_database=data["data"]
def get_pkmn(name):
    if name not in pkmn_database:
        return None
    pkmn=pkmn_database[name]
    return {
        "name": name,
        "usage": pkmn["usage"],
        "moves": pkmn["Moves"],
        "items": pkmn["Items"],
        "abilities": pkmn["Abilities"],
        "spreads": pkmn["Spreads"],
        "team-mates": pkmn["Teammates"],
        "checks and Counters": pkmn["Checks and Counters"] 
    }
def get_category(name, category):
    return pkmn_database[name][category]