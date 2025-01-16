from faker import Faker
import requests
import json
import random

fake = Faker()
api_url = "http://example.com/api"  # Замените на ваш URL API

def generate_place_data(place_id):
    return {
        "place": {
            "name": fake.company(),
            "web": fake.domain_name(),
            "description": {
                "description_en": fake.paragraph(nb_sentences=5),
                "description_sp": fake.paragraph(nb_sentences=5)
            },
            "categoryId": str(fake.uuid4()),
            "address": {
                "cityId": str(fake.uuid4()),
                "latitude": round(random.uniform(-90, 90), 6),
                "longitude": round(random.uniform(-180, 180), 6),
                "mapsUrn": fake.word()
            },
            "images": [],
            "socialNetworks": {
                "facebook": fake.url(),
                "instagram": None,
                "site": None,
                "x": None,
                "google": None
            },
            "phones": [
                {
                    "number": fake.phone_number(),
                    "isCallable": random.choice([True, False]),
                    "isWhatsapp": random.choice([True, False])
                }
            ],
            "email": fake.email(),
            "schedule": [
                {
                    "dayOfWeek": day,
                    "timeStart": "12:30:00",
                    "timeEnd": "22:00:00",
                    "startOfBreak": None,
                    "endOfBreak": None
                } for day in range(7)
            ],
            "idTags": [str(fake.uuid4()) for _ in range(2)]
        }
    }

for i in range(1000):
    data = generate_place_data(i + 1)
    response = requests.post(api_url, json=data)
    print(f"Sent data for place ID {i + 1}: {response.status_code}, Response: {response.json()}")