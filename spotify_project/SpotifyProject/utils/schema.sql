DROP TABLE IF EXISTS Artist CASCADE;

CREATE TABLE Artist (
    art_ID CHAR(22),
    art_name CHAR(40),
    PRIMARY KEY (art_ID)
);

DELETE FROM Artist;

DROP TABLE IF EXISTS Album CASCADE;

CREATE TABLE Album (
    alb_ID CHAR(22),
    alb_name CHAR(40),
    alb_duration INTEGER, -- skal tilføjes/regnes i csv fil
    PRIMARY KEY (alb_ID)
);

DELETE FROM Album;

DROP TABLE IF EXISTS Song CASCADE;

CREATE TABLE Song (
    song_ID CHAR(22),
    song_name CHAR(40),
    track_num INTEGER,
    song_duration INTEGER, -- skal tilføjes/regnes i csv fil
    release_date DATE,
    PRIMARY KEY (song_ID)
);

DELETE FROM Song;

DROP TABLE IF EXISTS Has;

CREATE TABLE Has (
    alb_ID CHAR(22),
    art_ID CHAR(22),
    PRIMARY KEY (alb_ID, art_ID),
    FOREIGN KEY (alb_ID) REFERENCES Album,
    FOREIGN KEY (art_ID) REFERENCES Artist ON UPDATE NO ACTION
);

DELETE FROM Has;

DROP TABLE IF EXISTS Belongs_To;

CREATE TABLE Belongs_To (
    alb_ID CHAR(22),
    song_ID CHAR(22),
    PRIMARY KEY (alb_ID, song_ID),
    FOREIGN KEY (alb_ID) REFERENCES Album,
    FOREIGN KEY (song_ID) REFERENCES Song ON UPDATE NO ACTION
);

DELETE FROM Belongs_To;

DROP TABLE IF EXISTS Must_Have;

CREATE TABLE Must_Have ( -- instead of just an artist 'has ' a song
    art_ID CHAR(22),
    song_ID CHAR(22),
    PRIMARY KEY (art_ID, song_ID),
    FOREIGN KEY (art_ID) REFERENCES Artist,
    FOREIGN KEY (song_ID) REFERENCES Song
);

DELETE FROM Must_Have;

copy  Song(song_ID, song_name, track_num, song_duration, release_date)
            from '/Users/naomiknudsen/Desktop/spotify_project/SpotifyProject/dataset/tracks_features.csv'
            delimiter ','
            CSV HEADER;

-- INSERT INTO Song(song_ID, song_name, track_num, song_duration, release_date) VALUES ('7lmeHLHBe4nmXzuXc0HDjk','Testify',1,210133,'1999-11-02')