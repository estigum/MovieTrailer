"""
This is the movietrailerexception module
"""

__author__ = "Erik Stigum"
__copyright__ = "Copyright 2015, Movie Trailer Website"
__email__ = "estigum@gmail.com"
__version__ = "1.0"

class MovieTrailerException(Exception):
    """
    This is just a special exception for
    MovieTrailer error
    """
    def __init__(self, message):
        """
        The constructor
        :param message:
        :return:
        """
        super(MovieTrailerException, self).__init__(message)
        self.message = message
