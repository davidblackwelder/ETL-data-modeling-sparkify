# Data Modeling with Postgres

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

## Project Description
I will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Schema for Song Play Analysis
A star schema for this project because this is optimized for queries. My fact table (songplays) contains data such as songplay_id, artist_id, song_id, timestamp, and user_id to link it to the respective dimension tables. The dimension tables used were artists, songs, time, and users. All of the dimensional tables have a primary key derived from the fact table.

## Project Files
`db_config.py` Loads in your `.env` data for connecting to both your own default database as well as the sparkifydb.
`create_tables.py` drops and creates tables for the sparkifydb.
`etl.ipyn` reads and process a single file from `song_data` and `log_data` to load into the tables for sparkifydb. This contains the detailed instructions on the ETL process for each of the tables and is used to implement the `etl.py` file.
`etl.py` Reads and processes all the files from `song_data` and `log_data` and then loads them into the tables.
`sql_queries.py` Contains all the SQL commands and queries.
