import json
from datetime import datetime

print(f"Starter opdatering af links: {datetime.now().strftime('%d-%m-%Y %H:%M')}")

# Dine helt præcise links til begivenhederne
alle_events = [
    {
        "sted": "El Mundo",
        "titel": "Jazz Jam, Pop Jam mm.",
        "dato": "Ugentlige events",
        "beskrivelse": "Tjek de nyeste musik-events, jams og festaftener direkte på El Mundos officielle oversigt.",
        "link": "https://www.facebook.com/elmundo9000/events"
    },
    {
        "sted": "Facebook",
        "titel": "Relevante Begivenheder",
        "dato": "Personligt feed",
        "beskrivelse": "Dine personligt tilpassede begivenheder i nærheden baseret på dine interesser og netværk.",
        "link": "https://www.facebook.com/events?source=46&action_history=null"
    },
    {
        "sted": "SingleNordic",
        "titel": "Dating & Speeddating",
        "dato": "Kommende arrangementer",
        "beskrivelse": "Find de nyeste speeddating-events og singlefester i området via Billetto.",
        "link": "https://billetto.dk/users/singlenordic?utm_source=billetto+advertising&utm_medium=search+engines&utm_campaign=google&utm_content=1DK"
    }
]

# Gemmer resultatet direkte i events.json, som appen automatisk læser ind
with open('events.json', 'w', encoding='utf-8') as f:
    json.dump(alle_events, f, ensure_ascii=False, indent=4)

print("events.json er nu blevet opdateret med de korrekte links!")
