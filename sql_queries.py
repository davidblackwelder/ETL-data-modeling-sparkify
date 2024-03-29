# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

user_table_create = ("""
    CREATE TABLE users (
      user_id INT,
      first_name VARCHAR,
      last_name VARCHAR,
      gender CHAR(1),
      level VARCHAR(10),
      PRIMARY KEY (user_id)
    );
""")

artist_table_create = ("""
    CREATE TABLE artists (
       artist_id VARCHAR,
       name VARCHAR,
       location VARCHAR,
       latitude NUMERIC,
       longitude NUMERIC,
       PRIMARY KEY (artist_id)
    );
""")

song_table_create = ("""
    CREATE TABLE songs (
        song_id VARCHAR,
        title VARCHAR,
        artist_id VARCHAR,
        year INT,
        duration NUMERIC,
        PRIMARY KEY (song_id)
    );
""")

time_table_create = ("""
    CREATE TABLE time (
        start_time TIMESTAMP,
        hour INT,
        day INT,
        week INT,
        month INT,
        year INT,
        weekday INT,
        PRIMARY KEY (start_time)
    );
""")

songplay_table_create = ("""
    CREATE TABLE songplays (
      songplay_id SERIAL,
      start_time TIMESTAMP,
      user_id INT,
      level VARCHAR(10),
      song_id VARCHAR,
      artist_id VARCHAR,
      session_id INT,
      location VARCHAR,
      user_agent VARCHAR,
      PRIMARY KEY (songplay_id)
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (
        start_time,
        user_id,
        level,
        song_id,
        artist_id,
        session_id,
        location,
        user_agent
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO users (
        user_id,
        first_name,
        last_name,
        gender,
        level
    )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO NOTHING
""")

song_table_insert = ("""
    INSERT INTO songs (
        song_id,
        title,
        artist_id,
        year,
        duration
     )
     VALUES (%s, %s, %s, %s, %s)
     ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists (
            artist_id,
            name,
            location,
            latitude,
            longitude
     )
     VALUES (%s, %s, %s, %s, %s)
     ON CONFLICT (artist_id) DO NOTHING
""")

time_table_insert = ("""
    INSERT INTO time (
        start_time,
        hour,
        day,
        week,
        month,
        year,
        weekday
     )
     VALUES (%s, %s, %s, %s, %s, %s, %s)
     ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id, artists.artist_id
FROM songs
JOIN artists ON songs.artist_id = artists.artist_id
WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create,
                        song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, artist_table_drop,
                      song_table_drop, time_table_drop, songplay_table_drop]
