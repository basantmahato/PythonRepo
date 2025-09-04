import requests

BASE_URL = "https://jsonplaceholder.typicode.com/user"


def get_user(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    if response.status_code== 200:
        print("Get Request Successful")
        print(response.json())
    else:
        print("get failed ",response.status_code)


def create_user():
    new_user ={
        "name": "John Doe",
        "username": "jandoe",
        "email":"xyz@mail.com"
    }
    response = requests.post(BASE_URL , json=new_user)

    if response.status_code == 201:
        print("Post request sucessful")
        print(response.json())

    else:
        print("Post failed . status code", response.status_code)


 def update_user(user_id):
    update_user = {
         "name": "John Doe",
        "username": "jandoe",
        "email":"xyz@mail.com"
    }
response = requests.put(f"{BASE_URL}/{USER_id}")
if response.status_code == 200:
    print("DELETE request succesfull!")
else:
    print("DELETE failed. status code:",response.status_code)
def main():
    print("\n--- performing GET ---")
    get_user(1) 

    print("\n--- performing POST ---")
    create_user()

    print("\n--- performing PUT ---")
    update_user(1)
    
    print("\n--- performing DELETE ---")
    delete_user(1)      
