import requests

url = "https://imdb8.p.rapidapi.com/title/find"

querystring = {"q":"game of thr"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "b6661d4409msh2cf7114e85e0ed5p128eb8jsnd144634fcc34"
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()

for item in response['results']:
    print('********************************************************')
    for k, v in item.items():
        print(f"{k} -> {v}")
