from faker import Faker
import requests
import json
import random

fake = Faker()
api_url = "https://backend.guider.pro/api/v2/Place/create"


def generate_place_data(place_id):
    return {
        "place": {
            "name": fake.company(),
            "web": fake.domain_name(),
            "description": {
                "description_en": fake.paragraph(nb_sentences=5),
                "description_sp": fake.paragraph(nb_sentences=5),
            },
            "categoryId": "06a32bc7-8ddd-434d-a36d-764105a31123",  # str(fake.uuid4()),
            "address": {
                "cityId": "0a708102-4476-4613-ada7-aacda3f61072",  # str(fake.uuid4()),
                "latitude": round(random.uniform(-90, 90), 6),
                "longitude": round(random.uniform(-180, 180), 6),
                "mapsUrn": fake.word(),
            },
            "images": [],
            "socialNetworks": {
                "facebook": fake.url(),
                "instagram": None,
                "site": None,
                "x": None,
                "google": None,
            },
            "phones": [
                {
                    "number": fake.phone_number(),
                    "isCallable": random.choice([True, False]),
                    "isWhatsapp": random.choice([True, False]),
                }
            ],
            "email": fake.email(),
            "schedule": [
                {
                    "dayOfWeek": day,
                    "timeStart": "12:30:00",
                    "timeEnd": "22:00:00",
                    "startOfBreak": None,
                    "endOfBreak": None,
                }
                for day in range(7)
            ],
            "idTags": [
                "0819bc43-7b97-4bfc-93d6-c145d1253fd5"
            ],  # [str(fake.uuid4()) for _ in range(2)],
        }
    }


for i in range(1):
    data = generate_place_data(i + 1)
    print(data)
    response = requests.post(api_url, json=data)
    print(
        f"Sent data for place ID {i + 1}: {response.status_code}, Response: {response.text}"
    )
