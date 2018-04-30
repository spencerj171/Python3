from pyfiglet import figlet_format
from termcolor import colored
import requests

url = "https://www.icanhazdadjoke.com/search"

print(figlet_format("Dad Joke 3000"))
topic = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
    url,
    headers={"Accept": "Application/JSON"},
    params={"term": topic, "limit": 1}
)

data = response.json()

if len(data) == 0:
    print(f"Sorry, I don't have any jokes about {topic}. Please try again")
elif len(data) == 1:
    print(f"I've got one joke about {topic}. Here it is:")
    print(data["results"][0]["joke"])
else:
    print(f"I've got {len(data)} jokes about {topic}. Here's one:")
    print(data["results"][0]["joke"])
