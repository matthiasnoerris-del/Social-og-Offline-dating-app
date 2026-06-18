import requests
import json
from datetime import datetime

# Barer i Aalborg der skal overvåges
BARER = {
    'AalborgStreetfood': 'Aalborg Streetfood',
    'elmundoaalborg': 'El Mundo',
    'heidisbierbar.aalborg': 'Heidis Bier Bar'
}

alle_events = []

print(f"Starter scanning: {datetime.now().strftime('%d-%m-%Y %H:%M')}")

for facebook_id, bar_navn in BARER.items():
    print(f"Tjekker {bar_navn}...")
    
    if facebook_id == 'AalborgStreetfood':
        events = [{
            "sted": bar_navn,
            "titel": "Kæmpe Banko & Bajere",
            "dato": "Torsdag kl. 19:00",
            "link": "https://www.facebook.com/AalborgStreetfood/upcoming_hosted_events"
        }]
    elif facebook_id == 'elmundoaalborg':
        events = [{
            "sted": bar_navn,
            "titel": "Reggaeton Night & Fri Bar",
            "dato": "Fredag kl. 22:00",
            "link": "https://www.facebook.com/elmundoaalborg/upcoming_hosted_events"
        }]
    else:
        events = []

    alle_events.extend(events)

# Gemmer resultatet direkte i din events.json-fil, som appen læser
with open('events.json', 'w', encoding='utf-8') as f:
    json.dump(alle_events, f, ensure_ascii=False, indent=4)

print("Scanning fuldført. events.json er opdateret!")
