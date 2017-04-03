import webbrowser


class Movie:
    """A class used to store movie related information.

    Attributes:
        title: A string indicate the title of the movie.
        poster_image_url: A string indicate the url of the movie poster image.
        trailer_youtube_url: A string indicate the url of the movie trailer on youtube.
    """

    def __init__(self, title, poster_image, trailer):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """Show the movie trailer when clicked on the movie poster"""
        webbrowser.open(self.trailer_youtube_url)
