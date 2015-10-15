"""
This is the unittest for media module
"""
__author__ = "Erik Stigum"
__copyright__ = "Copyright 2015, Movie Trailer Website"
__email__ = "estigum@gmail.com"
__version__ = "1.0"


import unittest
import media
from movietrailerexception import MovieTrailerException
import logging


class MediaUnitTest(unittest.TestCase):
    """
    This is the unittest for Media class
    """
    def setUp(self):
        """
        This creates a media object to
        test for each unit tests
        :return:
        """
        self.logger = logging.getLogger()
        self.new_media = media.Media(self.logger)


    def test_read_movie_file(self):
        """
        This test read_movie_file method
        :return:
        """
        self.new_media.read_movie_file("moviedata-test1.csv")
        self.assertEqual(len(self.new_media.movies), 2)
        self.assertEqual(self.new_media.movies[0].title, "Point Break")
        self.assertEqual(self.new_media.movies[1].title, "Dirty Dancing")

    def test_read_movie_file_invalid(self):
        """
        This test read_movie_file with
        invalid formatted movie file
        :return:
        """
        try:
            self.new_media.read_movie_file("moviedata-test2.csv")
        except MovieTrailerException, error:
            self.assertEqual(error.message, "Invalid record: Point Break;http://ia.media-imdb.com/images/M/"
                                           "MV5BMTIwNTk1MTgxMF5BMl5BanBnXkFtZTcwODI4NDUzMQ@@._V1_UY1200_CR126,0,630,1200_AL_.jpg"
                                           ";https://www.youtube.com/watch?v=0hd49bnStgU\n")

    def test_generate_movie_data_invalid_filename(self):

        try:
            self.new_media.generate_movie_data("MovieFile","erik.csv")
        except IOError, error:
            self.assertEqual(error.message, "Can't open file erik.csv")

    def test_generate_movie_data_invalid_mode(self):
        """
        This test generate_movie_data
        with invalid command
        :return:
        """
        try:
            self.new_media.generate_movie_data(None,"moviedata-test1.csv")
        except MovieTrailerException, error:
            self.assertEqual(error.message, "Usage: <configFile>")

    def test_generate_movie_data(self):
        """
        This test generate_movie_data using
        a valid movie file
        :return:
        """
        self.new_media.generate_movie_data("MovieFile", "moviedata-test1.csv")
        self.assertEqual(len(self.new_media.movies), 2)
        self.assertEqual(self.new_media.movies[0].title, "Point Break")
        self.assertEqual(self.new_media.movies[1].title, "Dirty Dancing")

if __name__ == "__main__":
    unittest.main()
