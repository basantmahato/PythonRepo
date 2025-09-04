import requests

def fetch_user_random():
    url= "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data ["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return  username , country 
    else:
        raise Exception ("failed to fetch data")
    
def main():
    try:
        username, country = fetch_user_random()
        print(f"username:{username} \ncountry: {country}")

    except Exception as e:
        print(str(e))
        
if __name__ == "__main__":
    main()      


