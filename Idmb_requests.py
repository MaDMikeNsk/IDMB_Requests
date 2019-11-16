import requests


class IMDb:
    def __init__(self):
        self.__apikey = '9bcb50b'
        self.__url = f"http://www.omdbapi.com/?apikey={self.__apikey}"

    def get_movies_by_title(self, title):
        querystring = {"s": title, "r": "json"}
        response = requests.get(self.__url, querystring).json()
        if response['Response'] == 'True':
            return [item['Title'] for item in response['Search']]
        else:
            return print(f'Unfortunately, there is no movie "{title}" in our base')

# querystring = {"s": "Avengers", "r": "json", "y": "2008"}
