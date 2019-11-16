import requests

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

querystring = {"r": "json", "s": "Avengers"}

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "b6661d4409msh2cf7114e85e0ed5p128eb8jsnd144634fcc34"
    }

response = requests.get(url, headers=headers, params=querystring).json()
print(f"Number of films: {len(response['Search'])}")
print('**************')
for item in response['Search']:
    print(item['Title'])