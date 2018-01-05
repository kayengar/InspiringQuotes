# InspiringQuotes
This application scrapes interesting quotes of authors from the website www.goodreads.com. The user has to enter the author of their choice, and a threshold to limit the number of quotes that they wish to see. 

The application is configured to run on port 5000 of localhost. The user passes an author name to the endpoint and receives all the quotes written by the author. 
Example: http://localhost:5000/gandhi
The response is a JSON with the author name as key anda list of all his quotes as the value. The response is persisted onto a MongoDB database so that the next time a user requests the same author's quote, it can be fetched from the database instead of scraping from the website again.

Installation instructions:

Install Flask:
$ sudo pip install Flask

Install MongoDB:
$ sudo apt-get install mongodb
$ sudo service mongodb start

Steps to run application:

1. Open terminal and type the following command:
    $ python app.py
    
2. Open the browser and enter:
   http://localhost:5000/<author-name>
   

Happy reading and getting inspired! 


