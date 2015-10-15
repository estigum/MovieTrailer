"""
This is the Movie Module
"""
__author__ = "Erik Stigum"
__copyright__ = "Copyright 2015, Movie Trailer Website"
__email__ = "estigum@gmail.com"
__version__ = "1.0"

class Movie(object):
    """
    This will store an instance of a given Movie.
    """

    def __init__(self):
        """
        This is the constructor. I just set the
        values to None
        :return:
        """
        self.trailer_youtube_url = None
        self.poster_image_url = None
        self.title = None
        self.director = None
        self.actors = None
        self.release_date = None

    def set_trailer_youtube_url(self, url):
        """
        This will set the trailer YouTube url
        :param url:
        :return:
        """
        self.trailer_youtube_url = url

    def set_poster_image_url(self, url):
        """
        This will set the poster image url
        :param url:
        :return:
        """
        self.poster_image_url = url

    def set_title(self, title):
        """
        This will set the title
        :param title:
        :return:
        """
        self.title = title

    def set_director(self, director):
        """
        This will set the director
        :param director:
        :return:
        """
        self.director = director

    def set_actors(self, actors):
        """
        This will set the actors
        :param actors:
        :return:
        """
        self.actors = actors

    def set_release_date(self, release_date):
        """
        This will set the release_date
        :param release_date:
        :return:
        """
        self.release_date = release_date

    def get_trailer_youtube_url(self):
        """
        This gets the YouTube url
        :return youtube url:
        """
        return self.trailer_youtube_url

    def get_poster_image_url(self):
        """
        This gets the poster url
        :return poster url:
        """
        return self.poster_image_url

    def get_title(self):
        """
        This returns the title of the movie
        :return title:
        """
        return self.title

    def get_director(self):
        """
        This will get the director
        :return director:
        """
        return self.director

    def get_actors(self):
        """
        This will returns actors
        :return:
        """
        return self.actors

    def get_release_date(self):
        """
        This will return release_date
        :return:
        """
        return self.release_date
