import requests
import random
import time
from faker import Faker


fake = Faker()
api_url = "https://backend.guider.pro/api/v2/Place/create"

pool_citis_ids = [
    "c1c85c18-a79c-40d6-a0a1-cadbde6ca5c2",
    "79069099-6d8d-4c31-b6c2-ea36b44751bb",
    "01a12b06-baff-4353-9dda-9800acb1db03",
    "109c241f-a289-40b5-b4fc-a4038b52149a",
    "a3464f13-46a0-4fd1-8c9c-b519a85c162a",
    "bfc47d56-7bd3-4fc1-980b-ae4a23c01679",
    "ea5db683-8f28-4299-bc5f-8786642319d0",
    "ff639909-08a9-48a8-b710-1175b71fc696",
    "ff718973-c0c2-4eed-9c76-a889f9c53210",
]

pool_cat_ids = [
    "06a32bc7-8ddd-434d-a36d-764105a31123",
    "4766d235-ed80-4216-a417-7b1bf74e6712",
    "98c3395b-7ee3-495d-8aeb-04adef985d5a",
]


def generat_place_data():
    data = {
        "place.Name": fake.company(),
        "place.Web": fake.word() + "_" + fake.word(),
        "place.Description.Description_en": fake.paragraph(nb_sentences=3),
        "place.Description.Description_sp": fake.paragraph(nb_sentences=3),
        "place.CategoryId": random.choice(pool_cat_ids),
        "place.Address.CityId": random.choice(pool_citis_ids),
        "place.Address.Latitude": round(random.uniform(9.3, 11.7), 6),
        "place.Address.Longitude": round(random.uniform(-83.2, -85.3), 6),
        "place.Email": fake.email(),
        "place.Phones": fake.phone_number(),
        "place.Images[0].serialNumber": 1,
        "place.Address.MapsUrn": fake.url(),
        "place.SocialNetworks.Instagram": "@" + fake.domain_word(),
    }
    # print(data["place.Address.CityId"])
    # print(data["place.CategoryId"])
    return data


files = [
    (
        "place.Images[0].imageFile",
        (
            "image1.jpg",
            open("image1.jpg", "rb"),
            "image/jpeg",
        ),
    ),
    (
        "place.Images[0].imageFile",
        (
            "image.jpg",
            open("image.jpg", "rb"),
            "image/jpeg",
        ),
    ),
]

for _ in range(400):
    data = generat_place_data()
    response = requests.post(api_url, data=data, files=files)
    if response.status_code == 201:
        print(f"Ok, place #{_} create. Place {data['place.Name']}")
    else:
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    time.sleep(2)

# url = "https://backend.guider.pro/api/v2/Place/create"

# payload = {
#     "place.Name": "NewPlaceTest777",
#     "place.Web": "placeweb33777",
#     "place.Description.Description_en": "description",
#     "place.Description.Description_sp": "description",
#     "place.CategoryId": "06a32bc7-8ddd-434d-a36d-764105a31123",
#     "place.Address.CityId": "c1c85c18-a79c-40d6-a0a1-cadbde6ca5c2",
#     "place.Address.Latitude": "10",
#     "place.Address.Longitude": "10",
#     "place.Images[0].serialNumber": "1",
# }

# headers = {}

# response = requests.request("POST", url, headers=headers, data=payload, files=files)

# print(response.text)
