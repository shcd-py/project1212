import requests

class CreateUserTest:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_user(self, username, password):
        url = f"{self.base_url}/Account/v1/User"
        data = {"userName": username, "password": password}
        response = requests.post(url, json=data)
        if response.status_code == 201:
            print("User created successfully:", response.json())
        else:
            print(f"Error: {response.status_code} - {response.text}")
