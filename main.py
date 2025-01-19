from faker import Faker
import requests
import json
from random import choice, uniform
import time

fake = Faker()

API_URL_USER = "https://backend.guider.pro/api/v2/Account/register"


def create_fake_user():
    char = ("!", "?", "*", ".")
    password = fake.password(
        length=10,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True,
    ) + choice(char)
    data = {
        "email": fake.free_email(),
        "password": password,
    }
    print(data)
    # try:
    response = requests.post(API_URL_USER, json=data)
    print(response.status_code, response)
    # except Exception as e:
    #     print(str(e))


def main(num_requests):
    for _ in range(num_requests):
        create_fake_user()
        time.sleep(uniform(0.1, 0.7))


if __name__ == "__main__":
    main(100)
