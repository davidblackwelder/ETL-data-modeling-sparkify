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
      first_name VARCHAR NOT NULL,
      last_name VARCHAR NOT NULL,
      gender CHAR(1),
      level VARCHAR(10) NOT NULL,
      PRIMARY KEY (user_id)
    );
""")

artist_table_create = ("""
    CREATE TABLE artists (
       artist_id VARCHAR,
       name VARCHAR NOT NULL,
       location VARCHAR,
       latitude NUMERIC,
       longitude NUMERIC,
       PRIMARY KEY (artist_id)
    );
""")

song_table_create = ("""
    CREATE TABLE songs (
        song_id VARCHAR,
        title VARCHAR NOT NULL,
        artist_id VARCHAR NOT NULL,
        year INT NOT NULL,
        duration NUMERIC NOT NULL,
        PRIMARY KEY (song_id),
        FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
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
      start_time TIMESTAMP NOT NULL,
      user_id INT NOT NULL,
      level VARCHAR(10) NOT NULL,
      song_id VARCHAR NOT NULL,
      artist_id VARCHAR NOT NULL,
      session_id INT NOT NULL,
      location VARCHAR NOT NULL,
      user_agent VARCHAR NOT NULL,
      PRIMARY KEY (songplay_id),
      FOREIGN KEY (user_id) REFERENCES users (user_id),
      FOREIGN KEY (song_id) REFERENCES songs (song_id),
      FOREIGN KEY (artist_id) REFERENCES artists (artist_id),
      FOREIGN KEY (start_time) REFERENCES time (start_time)
    );
""")

# INSERT RECORDS

# songplay_table_insert = ("""
# """)

# user_table_insert = ("""
# """)

# song_table_insert = ("""
# """)

# artist_table_insert = ("""
# """)


# time_table_insert = ("""
# """)

# # FIND SONGS

# song_select = ("""
# """)

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create,
                        song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, artist_table_drop,
                      song_table_drop, time_table_drop, songplay_table_drop]
