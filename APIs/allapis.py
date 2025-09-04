import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

# 1. GET Request (Fetch user)
def get_user(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        print("GET Request Successful!")
        print(response.json())
    else:
        print("GET Failed. Status Code:", response.status_code)

# 2. POST Request (Create new user)
def create_user():
    new_user = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john@example.com"
    }
    response = requests.post(BASE_URL, json=new_user)
    if response.status_code == 201:
        print("POST Request Successful!")
        print(response.json())
    else:
        print("POST Failed. Status Code:", response.status_code)

# 3. PUT Request (Update user fully)
def update_user(user_id):
    updated_user = {
        "name": "Jane Doe",
        "username": "janedoe",
        "email": "jane@example.com"
    }
    response = requests.put(f"{BASE_URL}/{user_id}", json=updated_user)
    if response.status_code == 200:
        print("PUT Request Successful!")
        print(response.json())
    else:
        print("PUT Failed. Status Code:", response.status_code)

# 4. DELETE Request (Delete user)
def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        print("DELETE Request Successful!")
    else:
        print("DELETE Failed. Status Code:", response.status_code)

def main():
    print("\n--- Performing GET ---")
    get_user(1)

    print("\n--- Performing POST ---")
    create_user()

    print("\n--- Performing PUT ---")
    update_user(1)

    print("\n--- Performing DELETE ---")
    delete_user(1)

if __name__ == "__main__":
    main()