# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
from typing import List, Dict

app = FastAPI()

# Example vocabulary data
vocabularies = {
    "2024-02-13": [
        {"word": "Ephemeral", "definition": "Lasting for a very short time."},
        {"word": "Pernicious", "definition": "Having a harmful effect, especially in a gradual or subtle way."},
        {"word": "Ameliorate", "definition": "Make (something bad or unsatisfactory) better."},
        {"word": "Obfuscate", "definition": "Render obscure, unclear, or unintelligible."},
        {"word": "Plethora", "definition": "A large or excessive amount of (something)."}
    ]
}

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/today")
async def get_todays_vocabulary():
    today_str = date.today().isoformat()
    return {
        "date": today_str,
        "vocabularies": vocabularies.get(today_str, [])
    }
