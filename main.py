from faker import Faker
import requests
from random import choice

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
        "email": fake.email(domain="yandex.com"),
        "password": password,
    }
    print(data)
    try:
        response = requests.post(API_URL_USER, json=data)
        print(response.status_code, response.json())
    except Exception as e:
        print(str(e))


def main(num_requests):
    for _ in range(num_requests):
        create_fake_user()


if __name__ == "__main__":
    main(200)
