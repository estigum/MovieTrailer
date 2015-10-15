"""
This is the unittest for the
queryimdb module
"""

__author__ = "Erik Stigum"
__copyright__ = "Copyright 2015, Movie Trailer Website"
__email__ = "estigum@gmail.com"
__version__ = "1.0"

import unittest
import requests
import queryimdb
import bs4
import unicodedata
import logging
class QueryIMDBUnitTest(unittest.TestCase):
    """
    This is the class for queryimdb unit
    test.
    """
    def setUp(self):
        """
        setup data
        :return:
        """
        pass

    def test_get_titleid(self):
        """
        This will test getting the title id
        :return:
        """
        res = requests.get(queryimdb.get_imdb_search_url("Point Break", "1991"))
        self.assertEqual(queryimdb.get_titleid(res),"tt0102685")

    def test_get_movie_poster_url(self):
        """
        This test getting the movie
        poster url
        :return:
        """
        res = requests.get(queryimdb.get_imdb_movie_url("tt0102685"))
        mysoup = bs4.BeautifulSoup(res.text, "lxml")
        self.assertEqual(queryimdb.get_movie_poster_url(mysoup),
                         "http://ia.media-imdb.com/images/M/MV5BMTIwNTk1MT"
                         "gxMF5BMl5BanBnXkFtZTcwODI4NDUzMQ@@._V1_UY1200_CR126,0,630,1200_AL_.jpg")

    def test_get_imdb_movie_url(self):
        """
        This test getting the movie url
        :return:
        """
        self.assertEqual(queryimdb.get_imdb_movie_url("tt0102685"),
                         "http://www.imdb.com/title/tt0102685/")

    def test_get_release_date(self):
        """
        This test getting the release date
        :return:
        """
        res = requests.get(queryimdb.get_imdb_movie_url("tt0102685"))
        mysoup = bs4.BeautifulSoup(res.text, "lxml")
        temp = queryimdb.get_release_date(mysoup,"tt0102685")
        release_date = unicodedata.normalize('NFKD', temp).encode('ascii', 'ignore')
        self.assertEqual(release_date,' 12 July 1991')

    def test_get_director_actors(self):
        """
        This test getting the actors and
        director
        :return:
        """
        res = requests.get(queryimdb.get_imdb_movie_url("tt0102685"))
        mysoup = bs4.BeautifulSoup(res.text, "lxml")
        director, actors = queryimdb.get_director_actors(mysoup)
        self.assertEqual(director,"Kathryn Bigelow")
        self.assertEqual(actors,'  Patrick Swayze, Keanu Reeves, Gary Busey, Lori Petty')

    def test_get_youtube_trailer_ur(self):
        """
        This test getting the youtube
        url
        :return:
        """
        self.assertEqual(queryimdb.get_youtube_trailer_ur("Point Break", "1991"),
                         "https://www.youtube.com/watch?v=0hd49bnStgU")

    def test_read_movie_file(self):
        """
        This will test QueryIMDB clas
        and the method to read the movie
        file
        :return:
        """
        myquery = queryimdb.QueryIMDB(logging.getLogger())
        myquery.read_movie_file("moviename-test1.txt")
        self.assertEqual(len(myquery.movies),2)
        self.assertEqual(myquery.movies[0].title,"Point Break")

if __name__ == "__main__":
    unittest.main()
