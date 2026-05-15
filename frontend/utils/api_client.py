import requests

BASE_URL = "http://127.0.0.1:8000"


def get_profile_data(username):

    response = requests.get(
        f"{BASE_URL}/profile/{username}"
    )

    if response.status_code == 200:

        return response.json()

    return None


def get_wrapped_data(username):

    response = requests.get(
        f"{BASE_URL}/wrapped/{username}"
    )

    if response.status_code == 200:

        return response.json()

    return None
def get_resume_data(username):

    response = requests.get(
        f"{BASE_URL}/resume/{username}"
    )

    if response.status_code == 200:

        return response.json()

    return None