# ThroupleMusic_DIS

## Song database.
The application features a database containing pre-loaded songs, 
with the capability for users to add new songs. 
Additionally, users can utilize the search function to find artists, 
albums, and specific songs within the database.

## Installation.
- Clone the repository to the local system
- Install Python 3 for your system from [Python.org](https://www.python.org/)
- Install the required packages usin the following command: pip install -r requirements.txt

## How to run.
1. Create Server at port 5432

2. Create database in pgAdmin with the following attributes:
    name = MusicThrouple

    host = localhost

    port = 5432

    username = postgres

    password = DB_PASSWORD

3. Open a MusicThrouple=# in terminal and write:
    GRANT ALL PRIVILEGES ON DATABASE "MusicThrouple" TO postgres;

4. In regular Terminal. Be in folder of project and then write:
    . .venv/bin/activate

    python3 init_db.py

    export FLASK_APP=app
    
    export FLASK_ENV=development

    export DB_USERNAME="postgres"

    export DB_PASSWORD="DB_PASSWORD"
    
    flask run

## How to interact with the web application.

Click on 'All Data' to see all the songs in the database. 
Scroll down the page to see all the songs.

Click on 'Add Throuple' to add a song to the database, you need to write a song name, album title, and artist name. 
The track number and release date is not required. Click submit to add the song.

Click on 'Search' to search for a song, artist or album. If you choose 'Select filter:' as your filter, you will search the database for either song, artist or album.
You will search for songs, artist or albums that is 'ILIKE' (has words that contain your search input).
If your search doesn't match anything in the database, the message "No music was found for this search" will show in window. Else a table will be shown with what was found in the database.

## Comment about our implementation.
Originally we considered that a music-related application should use entities such as 'Artists', 'Albums', and 'Songs,' each with their own attributes and relationships. However, in our implementation, we have consolidated these entities into a single entity, 'MusicThrouple', which represents a combination of artists, albums, and songs. We still have those specific entities in our database, but it is current unused.

But for future iterations of the applicatio, it would be beneficial to actually use the different entities.

## Known frontend issues.
When you try to add a new Throuple, and it already exists a message telling the user that, will pop up. If you reload the webpage again the same message will pop-up. If you go to another page and back, nothing will happen, and if you ad a song afterwards succesfully, then nothong will happen when you go back to the add page.

### Credit.
This implementation is a collaborative effort by Aditya Fadhillah (hjg708), Naomi B. M. Knudsen (xng137), and Nikolaj F. Schaltz (bxz911) for a group assignment in Databases and Information Systems (DIS).
