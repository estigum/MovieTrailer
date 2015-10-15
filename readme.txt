Author: Erik Stigum
Email: estigum@gmail.com

This is my Movie Trailer Project for the first assignment of UDACITY Full Stack Web Developer.

I have a number of python files
1. movie.py - This hold the information about the movie. I have a set of methods for setting and getting data
    A. Title
    B. Poster url
    C. Youtube url
    D. Director
    E. Actors
    F. Release Date

 2. media.py  - This contains the main method and is responsible for reading either a movie file that contains all
 the information or going to IMDB/YouTube to get the necessary information about the movie. This program runs in two
 modes.
    A. File based - It load all the details on the movies from a file.
    B. IMDB/YouTube - This goes out to internet and screen scrapes IMDB for relevant information on a movie based on
    title and year.  It also gets the trailer link from YouTube.

 3. queryimdb.py  - This has a bunch of methods to query IMDB page for all the relevant information to build an instance
 of the movie class.  This also contains a class from reading a file that contains a list of movies and the year they came
 out.  I use that information to lookup the movie data on IMDB.

 4. movietrailerexception.py - This is a custom exception class for a Movie Trailer exception.

 5. fresh_tomatoes.py - I have made some modification such as adding director, actors, release date. Changed some of
 the methods for getting data from movie object.  changed a few minor things on the html.

Modules you may need to load on your computer to run this app
1. bs4 - BeautifulSoup  - I use this to parse the html page.
2. requests - This is to go out to the web.  Should have that on your machine already

 Unit Tests
 I have created a set of unit test files to test the functionality above.
 1. movie_unittest.py - This tests the movie class. 12 unit tests
 2. media_unittest.py - This test the media class. 5 Unit tests.  Uses some files to test.
    A. moviedata-test1.csv
    B. moviedata-test2.csv
 3. queryimdb_unittest.py - This test all the calls to IMDB and YouTube.  it also test the class QueryIMDB class. 7 unit tests. Uses one file for testing
    A. moviename-test1.txt

Configuration files
1. MovieFile.cfg - This is for the File Based Version. It will load moviedata.csv. This file contains six movies.
2. IMDB.cfg - This is for the IMDB/YouTube version.  It will load moviename.txt. This file contains six moves.

Running the program
1. File Based:  python media.py MovieFile.cfg
2. IMDB based: python media.py IMDB.cfg

Important files for running
1. moviename.txt - has the name and year of movies used for the IMDB configuration
2. moviedata.csv - has all the details about the movies for the file based one.