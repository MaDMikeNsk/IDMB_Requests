import requests

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

querystring = {"i": "tt4154796", "r":"json"}

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "b6661d4409msh2cf7114e85e0ed5p128eb8jsnd144634fcc34"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

for k, v in response.json().items():
    print(f"{k} -> {v}")

