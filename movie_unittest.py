"""
This is the module to test Movie class
"""

__author__ = "Erik Stigum"
__copyright__ = "Copyright 2015, Movie Trailer Website"
__email__ = "estigum@gmail.com"
__version__ = "1.0"


import movie
import unittest



class MovieUnitTest(unittest.TestCase):
    """
    This class is used to test the movie
    class
    """
    def setUp(self):
        """
        This will instantiate a new
        movie each time you run a one of
        the tests
        :return:
        """
        self.new_movie = movie.Movie()

    def test_set_title(self):
        """
        This will just test the set_title
        method
        :return:
        """
        self.new_movie.set_title("Point Break")
        self.assertEqual(self.new_movie.title, "Point Break")

    def test_set_poster_image_url(self):
        """
        This will test the set_poster_image_url
        method
        :return:
        """
        self.new_movie.set_poster_image_url("http://ia.media-imdb.com/images/M/"
                                            "MV5BMTIwNTk1MTgxMF5BMl5BanBnXkFtZTcwODI4NDUzMQ@@"
                                            "._V1_UY1200_CR126,0,630,1200_AL_.jpg")
        self.assertEqual(self.new_movie.poster_image_url, "http://ia.media-imdb.com/images/M/MV5"
                                                          "BMTIwNTk1MTgxMF5BMl5BanBnXkFtZTcwODI4ND"
                                                          "UzMQ@@._V1_UY1200_CR126,0,630,1200_AL_.jpg")

    def test_set_trailer_url(self):
        """
        This will test set_trailer_url
        method
        :return:
        """
        self.new_movie.set_trailer_youtube_url("https://www.youtube.com"
                                               "/watch?v=0hd49bnStgU")
        self.assertEqual(self.new_movie.trailer_youtube_url, "https://www.youtube"
                                                             ".com/watch?v=0hd49bnStgU")

    def test_set_director(self):
        """
        This will test the set_director
        method
        :return:
        """
        self.new_movie.set_director("Kathryn Bigelow")
        self.assertEqual(self.new_movie.director, "Kathryn Bigelow")

    def test_set_actors(self):

        self.new_movie.set_actors("Patrick Swayze, Jennifer Grey, Jerry Orbach, Cynthia Rhodes")
        self.assertEqual(self.new_movie.actors,"Patrick Swayze, Jennifer Grey, Jerry Orbach, Cynthia Rhodes")

    def test_set_release_date(self):
        """
        test set_release_date
        :return:
        """
        self.new_movie.set_release_date("12 July 1991")
        self.assertEqual(self.new_movie.release_date,"12 July 1991")


    def test_get_title(self):
        """
        This will test the get_title
        method
        :return:
        """
        self.new_movie.set_title("Point Break")
        self.assertEqual(self.new_movie.get_title(), "Point Break")

    def test_get_poster_image_url(self):
        """
        This will test get_poster_image_url
        method
        :return:
        """
        self.new_movie.set_poster_image_url("http://ia.media-imdb.com/images/M/MV5BMTIwNTk1MTgxMF5BMl"
                                            "5BanBnXkFtZTcwODI4NDUzMQ@@._V1_UY1200_CR126,0,630,1200_AL_.jpg")
        self.assertEqual(self.new_movie.get_poster_image_url(), "http://ia.media-imdb.com/images/M/MV5BMTIwNTk1MTgxM"
                                                                "F5BMl5BanBnXkFtZTcwODI4NDUzMQ@@._V1_UY1200_CR126,0,"
                                                                "630,1200_AL_.jpg")

    def test_get_trailer_url(self):
        """
        This will test get_trailer
        method
        :return:
        """
        self.new_movie.set_trailer_youtube_url("https://www.youtube.com/watch?v=0hd49bnStgU")
        self.assertEqual(self.new_movie.get_trailer_youtube_url(), "https://www.youtube.com/watch?v=0hd49bnStgU")

    def test_get_director(self):
        """
        This will test the get_director
        method
        :return:
        """
        self.new_movie.set_director("Kathryn Bigelow")
        self.assertEqual(self.new_movie.get_director(), "Kathryn Bigelow")

    def test_get_actors(self):

        self.new_movie.set_actors("Patrick Swayze, Jennifer Grey, Jerry Orbach, Cynthia Rhodes")
        self.assertEqual(self.new_movie.get_actors(),
                         "Patrick Swayze, Jennifer Grey, Jerry Orbach, Cynthia Rhodes")

    def test_get_release_date(self):
        """
        test get_release_date
        :return:
        """
        self.new_movie.set_release_date("12 July 1991")
        self.assertEqual(self.new_movie.get_release_date(),"12 July 1991")

if __name__ == "__main__":
    unittest.main()
