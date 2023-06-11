import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

load_dotenv()
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="MusicThrouple",
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
    )
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM MusicThrouple;')
    music = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', music=music)

@app.route('/add/', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        song = request.form['song']
        album = request.form['album']
        artists = request.form['artists']
        track_num = request.form['track_num']
        date = request.form['date']

        if track_num == '':
            track_num = None

        date = request.form['date']

        if date == '':
            date = None

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('SELECT throuple_artists, throuple_album, throuple_name \
                        FROM MusicThrouple WHERE LOWER(throuple_artists) = LOWER(%s) AND \
                        LOWER(throuple_album) =  LOWER(%s) AND LOWER(throuple_name) = \
                        LOWER(%s);', (artists, album, song))
        
        if cur.fetchone() == None:
            cur.execute('INSERT INTO MusicThrouple (throuple_artists, throuple_album, throuple_name, track_number, release_date)'
                    'VALUES (%s, %s, %s, %s, %s)',
                    (artists, album, song, track_num, date))
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('index'))
        else:
            cur.close()
            conn.close()
            return redirect(url_for('add', song_added='false'))

    return render_template('add.html', song_added=request.args.get('song_added'))

@app.route('/search/', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        filter_music = request.form['filter_music']
        filter = request.form['filter']
        conn = get_db_connection()
        cur = conn.cursor()
        
        if filter_music == "song_choice":
            cur.execute('SELECT * FROM MusicThrouple WHERE \
                        LOWER(throuple_name) ILIKE LOWER(%s)', 
                        ('%' + filter + '%',))

        elif filter_music == 'artists_choice':
            cur.execute('SELECT * FROM MusicThrouple WHERE \
                        LOWER(throuple_artists) ILIKE LOWER(%s)',
                        ('%' + filter + '%',))

        elif filter_music == 'album_choice':
            cur.execute('SELECT * FROM MusicThrouple WHERE \
                        LOWER(throuple_album) ILIKE LOWER(%s)',
                        ('%' + filter + '%',))
        else: 
            cur.execute('SELECT * FROM MusicThrouple WHERE \
                        LOWER(throuple_artists) ILIKE LOWER(%s) OR \
                        LOWER(throuple_album) ILIKE LOWER(%s) OR \
                        LOWER(throuple_name) ILIKE LOWER(%s)',
                        ('%' + filter + '%', '%' + filter + '%', '%' + filter + '%'))

        filter = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        return render_template('search.html', filter=filter)
    return render_template('search.html')