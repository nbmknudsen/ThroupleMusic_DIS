import psycopg2
import os
import time 

from dotenv import load_dotenv
from choices import df

load_dotenv()

if __name__ == '__main__':
    conn = psycopg2.connect(
        host="localhost",
        # database=os.getenv('DB_NAME'),
        # user=os.getenv('DB_USERNAME'),
        # password=os.getenv('DB_PASSWORD')
        database=os.getenv('SpotifyProject'),
        user=os.getenv('postgres'),
        password=os.getenv('DB_PASSWORD')
        
    )

    with conn.cursor() as cur:
        # Run schema.sql
        with open('schema.sql') as db_file:
            cur.execute(db_file.read())

            # Import all data from the tracks_features dataset, song 
            all_songs = list(
                map(lambda x: tuple(x),
                    # df[['id', 'name', 'album', 'album_id', 'artists', 'artist_ids', 'track_number', 'disc_number', 'explicit', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature', 'year', 'release_date']].to_records(index=False))
                    df[['id', 'name', 'track_number', 'duration_ms', 'release_date']].to_records(index=False))
            )
            # Import all data from the tracks_features dataset, artist
            all_artists = list(
                map(lambda x: tuple(x),
                    # df[['id', 'name', 'album', 'album_id', 'artists', 'artist_ids', 'track_number', 'disc_number', 'explicit', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature', 'year', 'release_date']].to_records(index=False))
                    df[['artist_ids', 'artists']].to_records(index=False))
            )

            all_albums= list(
                map(lambda x: tuple(x),
                    # df[['id', 'name', 'album', 'album_id', 'artists', 'artist_ids', 'track_number', 'disc_number', 'explicit', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature', 'year', 'release_date']].to_records(index=False))
                    df[['album_id', 'album']].to_records(index=False))
            )


            # time.strftime('%Y-%m-%d')
            args_str = ','.join(cur.mogrify("(%s, %s, %d, %d, '%s')", i).decode('utf-8') for i in all_songs)
            cur.execute("INSERT INTO Song (song_ID, song_name, track_num, song_duration, release_date) VALUES " + args_str)

            # time.strftime('%Y-%m-%d')
            args_str = ','.join(cur.mogrify("(%s, %s)", i).decode('utf-8') for i in all_artists)
            cur.execute("INSERT INTO Artist (art_ID, art_name) VALUES " + args_str)

            # time.strftime('%Y-%m-%d')
            args_str = ','.join(cur.mogrify("(%s, %s, %d)", i).decode('utf-8') for i in all_albums)
            cur.execute("INSERT INTO Album (alb_ID, alb_name, alb_duration) VALUES " + args_str)

            conn.commit()
            
    conn.close()