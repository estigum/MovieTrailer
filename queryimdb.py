"""
This is the query imdb module
This will get the movie data from
both imdb and youtube
"""

__author__ = "Erik Stigum"
__copyright__ = "Copyright 2015, Movie Trailer Website"
__email__ = "estigum@gmail.com"
__version__ = "1.0"

import requests
import bs4
import movie
import unicodedata
from movietrailerexception import MovieTrailerException


def get_titleid(res):
    """
    This will get the title ID for an IMDB database
    This is needed to lookup info on the movie.
    :param res:
    :return titleid:
    """
    mysoup = bs4.BeautifulSoup(res.text, "lxml")
    value = mysoup.select("div span")
    for val in value:
        strval = str(val)
        if "data-tconst" in strval:
            return val["data-tconst"]
    return None


def get_movie_poster_url(mysoup):
    """
    This will get the movie poster url
    :param mysoup:
    :return url:
    """
    value = mysoup.select("link")
    for val in value:
        if "href" in val.attrs:
            url = val["href"]
            if ".jpg" in url:
                return url
    return None

def get_release_date(mysoup, title_id):
    """
    This will get the release date
    :param mysoup:
    :param title_id:
    :return release_date:
    """
    search_item = "/title/" + title_id +"/"
    value = mysoup.select("a")
    for val in value:
        if "href" in val.attrs:
            if search_item in val["href"]:
                print val.attrs
                if "title" in val.attrs:
                    if "See all release dates" in val.attrs["title"]:
                        return val.contents[0]
    return None


def get_director_actors(mysoup):
    """
    This will get the director
    and actors from IMDB
    :param mysoup:
    :return:
    """
    director = None
    actors = None
    value = mysoup.select("meta")
    for val in value:
        if "content" in val.attrs:
            content = val["content"]
            if "Directed by" in content:
                if isinstance(content, unicode):
                    content = unicodedata.normalize('NFKD', content).encode('ascii', 'ignore')
                temp = content.split(".")
                if len(temp) > 2:
                    director = temp[0].replace("Directed by ", "")
                    actors = temp[1].replace("With ", "")
                    return director, actors
    return director, actors


def get_youtube_trailer_ur(moviename, year):
    """
    This goes out to YouTube to query for the
    trailer
    param moviename:
    :param year:
    :return url:
    """
    res = requests.get("https://www.youtube.com/results?search_query="
                        + moviename + "+trailer+" + year)
    mysoup = bs4.BeautifulSoup(res.text, "lxml")
    value = mysoup.select("div")
    for val in value:
        if "data-context-item-id" in val.attrs:
            return "https://www.youtube.com/watch?v=" \
                    + val["data-context-item-id"]

    return None

def get_imdb_search_url(moviename, year):
    """
    This will return the URL to search a given
    movie for a given year
    :param moviename:
    :param year:
    :return url:
    """
    return "http://www.imdb.com/search/title?release_date=" \
            + year + "," + year + "&title=" + moviename

def get_imdb_movie_url(titleid):
    """
    This will get the actual movie url
    based on the IMDB titleId
    :param titleid:
    :return url:
    """
    return "http://www.imdb.com/title/" + titleid + "/"

class QueryIMDB(object):
    """
    This is the class to Query IMDB for the Movie Poster
    It also is used to go out to Youtube.  I was originally
    going to get the trailer from IMDB, but you can't put
    it in an iframe
    """

    def __init__(self, logger):
        """
        This is the constructor
        :return:
        """
        self.movies = []
        self.logger = logger

    def read_movie_file(self, filename):
        """
        This will move the movie file. The
        file contains moviename, year of movie
        :param filename:
        :return:
        """
        try:
            movie_file = open(filename, "r")
        except IOError:
            raise IOError("Can't open file " + filename)
        else:
            for line in movie_file:
                temp = line.split(";")
                if len(temp) == 2:
                    new_movie = movie.Movie()
                    title = temp[0]
                    year = temp[1].rstrip('\n')
                    new_movie.set_title(title)
                    res = requests.get(get_imdb_search_url(title, year))
                    title_id = get_titleid(res)
                    if title_id:
                        res = requests.get(get_imdb_movie_url(title_id))
                        mysoup = bs4.BeautifulSoup(res.text, "lxml")
                        new_movie.set_poster_image_url(get_movie_poster_url(mysoup))
                        new_movie.set_trailer_youtube_url(get_youtube_trailer_ur(title, year))
                        director, actors = get_director_actors(mysoup)
                        new_movie.set_director(director)
                        new_movie.set_actors(actors)
                        release_date = get_release_date(mysoup,title_id)
                        new_movie.set_release_date(release_date)
                        self.movies.append(new_movie)
                        self.logger.info("Adding Movie Title: " + new_movie.get_title())
                else:
                    raise MovieTrailerException("Invalid record: " + line)
        finally:
            if "movie_file" in locals():
                movie_file.close()
