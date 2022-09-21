import requests
BASE_ENDPOINT = "http://127.0.0.1:5000"
AUTH_ENDPOINT = BASE_ENDPOINT + "/auth"


login_params = {
    "username": "admin",
    "password": "123"
}

auth_response = requests.post(AUTH_ENDPOINT, json=login_params, headers={'Content-Type': 'application/json'})
# print(auth_response.json())
token = auth_response.json()["access_token"]


item_params = {
    "name": "watch",
    "price": 15000.25
}
CREATE_ITEM_ENDPOINT= BASE_ENDPOINT + f"/item/{item_params['name']}"
cr_response = requests.post(
    CREATE_ITEM_ENDPOINT,
    headers={"Authorization": f"JWT {token}", 'Content-Type': 'application/json'},
    json=item_params
    )
print(cr_response.text)

update_params = {
    "name": "necklace",
    "price": 27455.99
}
UPDATE_ENDPOINT= BASE_ENDPOINT + f"/item/{update_params['name']}"
update_response = requests.put(
    UPDATE_ENDPOINT,
    json=update_params
)
print(update_response.text)

DELETE_ENDPOINT = CREATE_ITEM_ENDPOINT
del_response = requests.delete(DELETE_ENDPOINT, headers={'Authorization': f'JWT {token}'})
print(del_response.text)
