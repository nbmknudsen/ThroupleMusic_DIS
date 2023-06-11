import psycopg2
import os
import pandas as pd
from dotenv import load_dotenv
import numpy as np
from psycopg2.extensions import register_adapter, AsIs
register_adapter(np.int64, AsIs)

DATASET_PATH = os.path.join('dataset', 'tracks_test.csv') 
df = pd.read_csv(DATASET_PATH, sep=';')

load_dotenv()
conn = psycopg2.connect(
        host="localhost",
        database="MusicThrouple",#os.getenv('DB_NAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
    )

with conn.cursor() as cur:
    # Run schema.sql
    with open('schema.sql') as db_file:
        cur.execute(db_file.read())
        print("opened schema.sql")

    # Import all data from the tracks_features dataset, song 
    all_songs = list(
        map(lambda x: tuple(x),
            df[['id', 'name', 'track_number', 'release_date']].to_records(index=False))
            )
    # Import all data from the tracks_features dataset, artist
    all_artists = list(set(
        map(lambda x: tuple(x),
            df[['artist_ids', 'artists']].to_records(index=False)))
    )

    # Import all data from the tracks_features dataset, album 
    all_albums= list(set(
        map(lambda x: tuple(x),
            df[['album_id', 'album']].to_records(index=False)))
    )

    # Import all data from the tracks_features dataset, artist, album , song, track number, release date
    all_throuples= list(set(
        map(lambda x: tuple(x),
            df[['artists', 'album', 'name', 'track_number', 'release_date']].to_records(index=False)))
    )


    args_str = ','.join(cur.mogrify("(%s, %s, %s, %s)", i).decode('utf-8') for i in all_songs)
    cur.execute("INSERT INTO Song (song_ID, song_name, track_num, release_date) VALUES " + args_str)

    args_str1 = ','.join(cur.mogrify("(%s, %s)", i).decode('utf-8') for i in all_artists)
    cur.execute("INSERT INTO Artist (art_ID, art_name) VALUES " + args_str1)

    args_str2 = ','.join(cur.mogrify("(%s, %s)", i).decode('utf-8') for i in all_albums)
    cur.execute("INSERT INTO Album (alb_ID, alb_name) VALUES " + args_str2)

    args_str3 = ','.join(cur.mogrify("(%s, %s, %s, %s, %s)", i).decode('utf-8') for i in all_throuples)
    cur.execute("INSERT INTO MusicThrouple (throuple_artists, throuple_album, throuple_name, track_number, release_date) VALUES " + args_str3)

    conn.commit()

    cur.close()        
    conn.close()