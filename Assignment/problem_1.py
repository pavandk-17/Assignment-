import requests
from bs4 import BeautifulSoup

# Enter the name of the actor
actor_name = input("Enter the name of the actor: ")

# Format the actor name for IMDb URL
formatted_name = actor_name.replace(" ", "+")

# IMDb URL to scrape
url = f"https://www.imdb.com/list/ls006979718/?sort=list_order,asc&st_dt=&mode=detail&page=1&keywords={formatted_name}"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object from the response text
soup = BeautifulSoup(response.text, 'html.parser')

# Find the list of films for the given actor
films = soup.find_all('h3', class_='lister-item-header')

# Print the filmography in descending order
for i, film in enumerate(films):
    print(f"{i+1}. {film.a.text}")
