# https://reqres.in/api/users?page=2

import requests
import json

url = "https://reqres.in/"
headers = {
    "x-api-key": "reqres-free-v1"
}

def get_api():
    api = url + "api/users?page=2"
    response = requests.get(api, headers=headers)
    assert response.status_code==200
    json_data = response.json()
    json_str = json.dumps(json_data,indent = 4)
    print(f"The users are: {json_str}")

# get_api()

def single_user():
    api = url + "api/users/2"
    response = requests.get(api, headers=headers)
    assert response.status_code==200
    json_data = response.json()
    json_str = json.dumps(json_data,indent = 4)
    print(f"The users are: {json_str}")

single_user()

def register_user():
    api = url + "api/register"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(api, json=payload, headers=headers)
    assert response.status_code==200
    json_data = response.json()
    json_str = json.dumps(json_data,indent = 4)
    print(f"User registered successfully {json_str}")

# register_user()

def update():
    api = url + "api/users/2"
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put(api, json=payload, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(f"User information is updated {json_str}")

# update()

def delete():
    api = url + "api/users/2"
    response = requests.delete(api, headers=headers)
    assert response.status_code == 204
    print(f"User deleted")

# delete()

   

def login():
    api = url + "api/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(api, json=payload, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(f"Login successful: {json_str}")

# login()


