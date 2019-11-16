from Idmb_requests import IMDb

session = IMDb()

movies = session.get_movies_by_title('Avengers')

if movies:
    print(movies)