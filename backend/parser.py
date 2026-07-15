import json
with open("data/gen9championsvgc2026regmb-1760.json","r",encoding="utf-8"
          )as f: 
    data=json.load(f)
pkmn_database=data["data"]
tot_pkmn=len(pkmn_database) 
def get_all_pokemon():
    return list(pkmn_database.keys())
        
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
def get_usage_ranking():
    ranking=[]
    for name in pkmn_database:
        ranking.append({
            "name": name,
            "usage": pkmn_database[name]["usage"]
        })
    ranking=sorted(ranking,key=lambda pokemon:pokemon["usage"],reverse=True)
    return ranking[:20]
def get_Usage(name):
    return {
        "name": name,
        "usage": pkmn_database[name]["usage"]
    }
def get_category(name, category):
    return pkmn_database[name][category]