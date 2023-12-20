import requests
import pandas as pd
from pprint import pprint 

# Extract
res = requests.get("https://hp-api.onrender.com/api/characters")
data = res.json()

# Transform
hp_characters = []

# Transform
hp_characters = []

for character in data:
    wand_length = character["wand"].get("length", None)  # Handle missing wand length
    hogwarts = {
        "name": character.get("name", ""),
        "ancestry": character.get("ancestry", ""),
        "house": character.get("house", ""),
        "role": "Student" if character.get("hogwartsStudent", False) else "Staff",
        "wand_length": wand_length
    }
    hp_characters.append(hogwarts)

df = pd.DataFrame(hp_characters)

# Load
df.to_csv("dwh/hp_characters.csv", index = False)

