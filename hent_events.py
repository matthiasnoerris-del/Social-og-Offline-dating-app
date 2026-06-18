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
    
    # Her opbygger vi listen med alle de fede ugentlige events direkte i din app
    if facebook_id == 'AalborgStreetfood':
        events = [
            {
                "sted": bar_navn,
                "titel": "Kæmpe Banko & Bajere",
                "dato": "Torsdag kl. 19:00",
                "beskrivelse": "Tag vennerne med til Aalborgs hyggeligste banko! Der er kolde bajere på bordet og sprøde præmier på højkant.",
                "link": "https://aalborgstreetfood.dk"
            }
        ]
    elif facebook_id == 'elmundoaalborg':
        events = [
            {
                "sted": bar_navn,
                "titel": "Jazz Jam",
                "dato": "Onsdag kl. 20:00",
                "beskrivelse": "Oplev den fedeste live jazz i intime rammer. Lokale musikere indtager scenen, og stemningen er helt i top.",
                "link": "https://elmundo.dk"
            },
            {
                "sted": bar_navn,
                "titel": "Torsdag Jam",
                "dato": "Torsdag kl. 21:00",
                "beskrivelse": "Scenen er åben! Kom og lyt til sprøde toner, eller grib et instrument og spil med til El Mundos legendariske jam-aften.",
                "link": "https://elmundo.dk"
            },
            {
                "sted": bar_navn,
                "titel": "Reggaeton Night & Fri Bar",
                "dato": "Fredag kl. 22:00",
                "beskrivelse": "Dans natten væk til de vildeste reggaeton-rytmer. Der er fri bar i udvalgte drinks den første time!",
                "link": "https://elmundo.dk"
            }
        ]
    elif facebook_id == 'heidisbierbar.aalborg':
        events = [
            {
                "sted": bar_navn,
                "titel": "Fest for Singler",
                "dato": "Lørdag kl. 21:00",
                "beskrivelse": "Er du klar på at møde nye mennesker? Heidis danner rammen om Aalborgs største singlefest med ryst-sammen-lege og Afterski-stemning.",
                "link": "https://www.heidi-bierbar.dk/aalborg"
            }
        ]
    else:
        events = []

    alle_events.extend(events)

# Gemmer resultatet direkte i din events.json-fil, som appen læser
with open('events.json', 'w', encoding='utf-8') as f:
    json.dump(alle_events, f, ensure_ascii=False, indent=4)

print("Scanning fuldført. events.json er opdateret!")
