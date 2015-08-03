#Movie Trailer Site
This project is a Python based, which allows a list of Media objects (Movies and TV Series) to be passed into a HTML page generator.
The HTML page (entertainment_center.html) generated shows information about a selection of Movies and TV Series. 

For Movies the page allows the user to view the trailer and story line. 

For TV Shows the page allows the user to view details about individual episodes in the series.

The page allows the data to be filtered based on the type of media and the episodes for tv shows can be filtered by season.

##Requirements
- Internet connection - required for displaying the poster images and YouTube trailers
- Python 2.7 - the code has been written and tested using Python version 2.7

##Running the code
In order to generate and open the HTML page (entertainment_center.html) you need to run entertainment_center.py

##Project Contents
- create_page.py - produces html page
- entertainment_center.py - main code file, stores the list of objects for Movies and TV Series
- media.py - contains the definitions for the media classes
- scripts.js - contains all JavaScript functions used by the HTML Page
- styles.css - contains the styles used by HTML Page

##Recognition
create_page.py is based on the fresh_tomatoes.py script found at https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py
