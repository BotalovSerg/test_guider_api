from faker import Faker
import requests
import json
from random import choice, uniform
import time

fake = Faker()

API_URL_USER = "http://194.195.86.113:8888/api/v2/Account/register"


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
    try:
        response = requests.post(API_URL_USER, json=data)
        if response.status_code == 201:
            return True
        # print(response.status_code, response.text)
    except Exception as e:
        print(str(e))


def main(num_requests):
    for _ in range(num_requests):
        if create_fake_user():
            print(f"User #{_} create.")
        time.sleep(uniform(0.1, 0.7))


if __name__ == "__main__":
    main(300)
