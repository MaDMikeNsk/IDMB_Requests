import requests


class IMDb:
    def __init__(self):
        self.__apikey = '9bcb50b'
        self.__url = f"http://www.omdbapi.com/?apikey={self.__apikey}"

    def get_moviesID_by_title(self, title):
        querystring = {"s": title, "r": "json"}
        response = requests.get(self.__url, querystring).json()
        if response['Response'] == 'True':
            return [item['imdbID'] for item in response['Search']]
        else:
            return print(f'Mistake! There is no movie "{title}" in our base')

    def get_movie_info(self, movie_id) -> dict:
        querystring = {"i": movie_id, "r": "json"}
        response = requests.get(self.__url, querystring).json()
        return response

    def is_actor_in_movie(self, looking_actor, movie_title) -> None:
        flag = False
        movies_id_list = self.get_moviesID_by_title(movie_title)
        if not movies_id_list:
            flag = False
        else:
            for id in movies_id_list:
                movie_info = self.get_movie_info(id)
                actors_string = movie_info['Actors']
                actors_list = [item.strip() for item in actors_string.split(',')]
                if looking_actor in actors_list:
                    print(f"Success! Actor {looking_actor} plays in '{movie_info['Title']}'")
                    flag = True
        if not flag and movies_id_list:
            return print(f"Unfortunate. Actor {looking_actor} NOT IN movie '{movie_title}'")

# 'Title': 'The Social Network', 'Year': '2010', 'Rated': 'PG-13', 'Released': '01 Oct 2010', 'Runtime': '120 min',
# 'Genre': 'Biography, Drama',
# 'Director': 'David Fincher',
# 'Writer': 'Aaron Sorkin (screenplay), Ben Mezrich (book)',
# 'Actors': 'Jesse Eisenberg, Rooney Mara, Bryan Barter, Dustin Fitzsimons',
# 'Language': 'English, French', 'Country':
# 'USA', 'Awards': 'Won 3 Oscars. Another 165 wins & 168 nominations.',
# 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '7.7/10'}, {'Source': 'Rotten Tomatoes', 'Value': '96%'},
# {'Source': 'Metacritic', 'Value': '95/100'}],
# 'Metascore': '95', 'imdbRating': '7.7', 'imdbVotes': '579,002',
# 'imdbID': 'tt1285016', 'Type': 'movie', 'DVD': '11 Jan 2011', 'BoxOffice': '$96,400,000',
# 'Production': 'Columbia Pictures', 'Website': 'N/A', 'Response': 'True'}

