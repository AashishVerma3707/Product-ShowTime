import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Product_ShowTime.settings")
import django
django.setup()
from ShowTime_app.models import Movies
import requests

# This Module is dedicated to Populate our Database with latest Shows

# Unable to use IMDB package particularly to get latest movie list as of the lack in proper package
# documentation, hence another API (https://www.themoviedb.org/) has been used for getting the same data.


api_key = "a843b2101af4fd0a7ae24c62cf0dd5f7"
base_url = "https://api.themoviedb.org/3"

r = requests.get(f"{base_url}/movie/upcoming", params={'api_key': api_key})
data = r.json()

# Got 20 entries from upcoming movies
for movie in data["results"]:
    title = movie['title']
    new_instance= Movies.objects.create(title=title)
    new_instance.save()


r = requests.get(f"{base_url}/movie/now_playing", params={'api_key':api_key})
data = r.json()

# Got 5 entries from already released movies in order of their release date.
for movie in data["results"][0:5]:
    title = movie['title']
    new_instance = Movies.objects.create(title=title)
    new_instance.save()


