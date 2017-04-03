import media
import fresh_tomatoes


# Define some movies as instances of the class Movie
pursuit_of_happyness = media.Movie("The Pursuit of Happyness",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=89Kq8SDyvfg")

idiots = media.Movie("3 Idiots",
                     "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=xvszmNXdM4w")

the_martian = media.Movie("The Martian",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=Ue4PCI0NamI")

inception = media.Movie("Inception",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")
snowden = media.Movie("Snowden",
                      "https://upload.wikimedia.org/wikipedia/en/c/ca/Snowden_film_poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=QlSAiI3xMh4")

hunger_games = media.Movie("Hunger Games",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

the_revenant = media.Movie("The Revenant",
                           "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=QRfj1VCg16Y")

the_matrix = media.Movie("The Matrix",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")

avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Create a list of movies objects
movies = [pursuit_of_happyness, idiots, the_martian, inception,
          snowden, hunger_games, the_revenant, the_matrix, avatar]

# Create and open an HTML file to display a web page of the movies
fresh_tomatoes.open_movies_page(movies)