"""
This is the Media module.  Contains the main
method tht will run this project
"""
__author__ = "Erik Stigum"
__copyright__ = "Copyright 2015, Movie Trailer Website"
__email__ = "estigum@gmail.com"
__version__ = "1.0"

import movie
import fresh_tomatoes
import sys
import queryimdb
from movietrailerexception import MovieTrailerException
import ConfigParser
import logging

class Media(object):
    """
    The Media class will load the data and then
    call the methods in fresh_tomatoes to generate
    the web page and display it.
    """
    def __init__(self, logger):
        """
        This is the constructor
        :return:
        """
        self.movies = []
        self.url_type = ""
        self.logger = logger

    def read_new_imdb(self, filename):
        """
        This will read a file lookup poster
        in IMDB and get trailer from
        YouTube
        :param filename:
        :return:
        """
        try:
            imdb = queryimdb.QueryIMDB(self.logger)
            imdb.read_movie_file(filename)
            self.movies = imdb.movies
        except:
            raise

    def read_movie_file(self, filename):
        """
        This will read the movie file and for each
        record create a movie object and add it to the
        movies array
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
                if len(temp) == 6:
                    new_movie = movie.Movie()
                    new_movie.set_title(temp[0])
                    new_movie.set_poster_image_url(temp[1])
                    new_movie.set_trailer_youtube_url(temp[2])
                    new_movie.set_director(temp[3])
                    new_movie.set_actors(temp[4])
                    release_date = temp[5].rstrip('\n')
                    new_movie.set_release_date(release_date)
                    self.movies.append(new_movie)
                    self.logger.info("Adding Movie Title: "
                                     + new_movie.get_title())
                else:
                    raise MovieTrailerException("Invalid record: " + line)

        finally:
            if "movie_file" in locals():
                movie_file.close()

    def __del__(self):
        """
        Destructor. Cleanup the array of data
        :return:
        """
        del self.movies[:]


    def generate_movie_data(self, mode, filename):
        """
        This will take the mode and file name
        Based on the mode it will either just read
        all information for a given movie from the
        file or look it up on IMDB and YouTube
        :param mode, filename:
        :return:
        """
        try:
            if mode == "MovieFile":
                self.read_movie_file(filename)
            elif mode == "IMDBLookup":
                self.read_new_imdb(filename)
            else:
                raise MovieTrailerException(get_valid_command_line_message())
        except:
            raise

def set_logger_mode(logger, mode):
    """
    This will set the logging mode
    for the logger
    :param logger:
    :param mode:
    :return:
    """
    if mode == "DEBUG":
        logger.setLevel(logging.DEBUG)
    elif mode == "INFO":
        logger.setLevel(logging.INFO)
    elif mode == "WARNING":
        logger.setLevel(logging.WARNING)
    elif mode == "ERROR":
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.INFO)

def get_logger():
    """
    This will get a new logger
    :return logger:
    """
    logger = logging.getLogger()

    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter("%(asctime)s %(name)-5s"
                               " %(levelname)-5s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

def get_valid_command_line_message():
    """
    This will just generate what you can pass on
    command line. We will print this if given
    invalid command line.
    :return text:
    """
    text = "Usage: <configFile>"
    return text

def main():
    """
    This is the main method.
    :return:
    """
    try:
        logger = get_logger()
        set_logger_mode(logger, "WARNING")

        if len(sys.argv) < 2:
            raise MovieTrailerException(get_valid_command_line_message())

        config_parser = ConfigParser.ConfigParser()
        config_parser.read(sys.argv[1])

        if not config_parser.has_option("run_mode", "mode"):
            raise MovieTrailerException("Invalid configuration:  Missing mode for run_mode")
        if not config_parser.has_option("run_mode", "filename"):
            raise MovieTrailerException("Invalid configuration:  Missing filename for run_mode")
        if not config_parser.has_option("logging", "mode"):
            raise MovieTrailerException("Invalid configuration:  Missing mode for logging")

        set_logger_mode(logger, config_parser.get("logging", "mode"))

        mode = config_parser.get("run_mode", "mode")
        filename = config_parser.get("run_mode", "filename")

        media = Media(logger)
        media.generate_movie_data(mode, filename)

        fresh_tomatoes.create_movie_tiles_content(media.movies)
        fresh_tomatoes.open_movies_page(media.movies)

    except (MovieTrailerException, IOError), error:
        logger.error(error.message)

if __name__ == "__main__":
    main()
