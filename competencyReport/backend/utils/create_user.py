import requests

URL = "http://127.0.0.1:5000/users"

def create_user(first, last, hobbies):
    user_data = {
        "first_name" : first,
        "last_name" : last,
        "hobbies" : hobbies
    }

    response = requests.post(URL, json=user_data)
    if response.status_code == 204:
        print("User successfully created")
    else: 
        print("Error: User was not created.")

# if the script is directly executed from the terminal
if __name__ == "__main__":
    print("CREATE USER")
    print("-" * 20)
    first = input("First name: ")
    last = input("Last name: ")
    hobbies = input("Hobbies: ")

    create_user(first, last, hobbies)