from typing import Dict

from psycopg2 import sql

from SpotifyProject import db_cursor, conn, app


class ModelMixin(dict):
    pass

class Song(ModelMixin):
    def __init__(self, song_data: Dict):
        super(Song, self).__init__(song_data)
        self.id = song_data.get('song_ID')
        self.name = song_data.get('song_name')
        self.track_num = song_data.get('track_num')
        self.duration = song_data.get('song_duration')
        self.release_date = song_data.get('release_date')
        # From JOIN w/ Belongs_To relation
        self.alb_id = song_data.get('alb_ID')
        # From JOIN w/ Must_Have relation
        self.art_id = song_data.get('art_ID')


class Artist(ModelMixin):
    def __init__(self, artist_data: Dict):
        super(Artist, self).__init__(artist_data)
        self.id = artist_data.get('art_ID')
        self.name = artist_data.get('art_name')
        # From JOIN w/ Has relation
        self.alb_id = artist_data.get('alb_ID')
        # From JOIN w/ Must_Have relation
        self.song_id = artist_data.get('song_ID')


class Album(ModelMixin):
    def __init__(self, album_data: Dict):
        super(Album, self).__init__(album_data)
        self.id = album_data.get('alb_ID')
        self.name = album_data.get('alb_name')
        self.duration = album_data.get('alb_duration')
        # From JOIN w/ Has relation
        self.art_id = album_data.get('art_ID')
        # From JOIN w/ Belongs_To relation
        self.song_id = album_data.get('song_ID')

class Has(ModelMixin):
    def __init__(self, has_data: Dict):
        super(Has, self).__init__(has_data)
        self.alb_id = has_data.get('alb_ID')
        self.art_id = has_data.get('art_ID')

class BelongsTo(ModelMixin):
    def __init__(self, belong_data: Dict):
        super(BelongsTo, self).__init__(belong_data)
        self.alb_id = belong_data.get('alb_ID')
        self.song_id = belong_data.get('song_ID')

class MustHave(ModelMixin):
    def __init__(self, must_data: Dict):
        super(MustHave, self).__init__(must_data)
        self.art_id = must_data.get('art_ID')
        self.song_id = must_data.get('song_ID')
