import requests
url = "http://api.open-notify.org/astros.json"

def people():
  response = requests.get(url).json()
  return response["number"]

def names():
  response = requests.get(url).json()
  for person in response["people"]:
    print(person["name"])

number = people()
guess= int(input("how many poeple do oyu think are in space right now?: "))

if guess < people():
    print(f"That is too High the number is {number}")
elif guess > people():
    print(f"Too low! {number} are in space right now")
elif guess == people():
    print("perceft!")
else:
    print("Invaild input!")