import requests
BASE_ENDPOINT = "https://storest-api.herokuapp.com" 
AUTH_ENDPOINT = BASE_ENDPOINT + "/auth"


login_params = {
    "username": "Frayo",
    "password": "Frayo123"
}

auth_response = requests.post(AUTH_ENDPOINT, json=login_params, headers={'Content-Type': 'application/json'})
# print(auth_response.json())
token = auth_response.json()["access_token"]


item_params = {
    "name": "watch",
    "price": 15000.25,
    "store_id": 2
}
CREATE_ITEM_ENDPOINT= BASE_ENDPOINT + f"/item/{item_params['name']}"
cr_response = requests.post(
    CREATE_ITEM_ENDPOINT,
    headers={"Authorization": f"JWT {token}", 'Content-Type': 'application/json'},
    json=item_params
    )
print(cr_response.text)

update_params = {
    "name": "watch",
    "price": 27455.99,
    "store_id": 2
}
UPDATE_ENDPOINT= BASE_ENDPOINT + f"/item/{update_params['name']}"
update_response = requests.put(
    UPDATE_ENDPOINT,
    headers={"Authorization": f"JWT {token}"},
    json=update_params
)
print(update_response.text)

DELETE_ENDPOINT = CREATE_ITEM_ENDPOINT
del_response = requests.delete(DELETE_ENDPOINT, headers={'Authorization': f'JWT {token}'})
print(del_response.text)
