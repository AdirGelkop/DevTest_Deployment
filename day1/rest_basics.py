import requests

#GET - getting info
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(f"Status code : {response.status_code}")
print(f"Response body : {response.json()}")

#POST - creating new info
new_user = {
    "name": "Adir",
    "email": "adir@test.com"
}
response = requests.post("https://jsonplaceholder.typicode.com/users", json=new_user)
print(f"Status code : {response.status_code}")
print(f"Response body : {response.json()}")

# PUT - updating info
updated_user = {"name": "Adir Updated", "email": "adir2@test.com"}
response = requests.put("https://jsonplaceholder.typicode.com/users/1", json=updated_user)
print(f"PUT Status: {response.status_code}")
print(f"Response body : {response.json()}")

# DELETE - deleting info
response = requests.delete("https://jsonplaceholder.typicode.com/users/1")
print(f"DELETE Status: {response.status_code}")
print(f"Response body : {response.json()}")
