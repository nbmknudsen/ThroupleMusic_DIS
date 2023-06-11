DROP TABLE IF EXISTS Artist CASCADE;

CREATE TABLE Artist (
    art_ID CHAR(26),
    art_name CHAR(60),
    PRIMARY KEY (art_ID)
);

-- DELETE FROM Artist;

DROP TABLE IF EXISTS Album CASCADE;

CREATE TABLE Album (
    alb_ID CHAR(22),
    alb_name CHAR(60),
    PRIMARY KEY (alb_ID)
);

-- DELETE FROM Album;

DROP TABLE IF EXISTS Song CASCADE;

CREATE TABLE Song (
    song_ID CHAR(22),
    song_name CHAR(60),
    track_num INTEGER,
    release_date DATE,
    PRIMARY KEY (song_ID)
);

-- DELETE FROM Song;

DROP TABLE IF EXISTS Has;

CREATE TABLE Has (
    alb_ID CHAR(22),
    art_ID CHAR(26),
    PRIMARY KEY (alb_ID, art_ID),
    FOREIGN KEY (alb_ID) REFERENCES Album,
    FOREIGN KEY (art_ID) REFERENCES Artist ON UPDATE NO ACTION
);

-- DELETE FROM Has;

DROP TABLE IF EXISTS Belongs_To;

CREATE TABLE Belongs_To (
    alb_ID CHAR(22),
    song_ID CHAR(22),
    PRIMARY KEY (alb_ID, song_ID),
    FOREIGN KEY (alb_ID) REFERENCES Album,
    FOREIGN KEY (song_ID) REFERENCES Song ON UPDATE NO ACTION
);

-- DELETE FROM Belongs_To;

DROP TABLE IF EXISTS Must_Have;

CREATE TABLE Must_Have ( -- instead of just an artist 'has ' a song
    art_ID CHAR(26),
    song_ID CHAR(22),
    PRIMARY KEY (art_ID, song_ID),
    FOREIGN KEY (art_ID) REFERENCES Artist,
    FOREIGN KEY (song_ID) REFERENCES Song
);

-- DELETE FROM Must_Have;

DROP TABLE IF EXISTS Music;
CREATE TABLE Music(
  id CHAR(22),
  song_name CHAR(60),
  album CHAR(60),
  album_id CHAR(22),
  artists CHAR(60),
  artist_ids CHAR(26),
  track_number INTEGER,
  release_date DATE,
  PRIMARY KEY (id)
);

-- DELETE FROM Music;

DROP TABLE IF EXISTS MusicThrouple;
CREATE TABLE MusicThrouple(
  throuple_artists CHAR(60),
  throuple_album CHAR(60),
  throuple_name CHAR(60),
  track_number INTEGER,
  release_date DATE,
  PRIMARY KEY (throuple_artists, throuple_album, throuple_name)
);

-- DELETE FROM MusicThrouple;

