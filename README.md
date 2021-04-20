# Spotify Data

`scrape.py` - This script pulls recently played songs from a user's Spotify account via the API. Because the Spotify API only returns the last 50 tracks played, I scheduled this script to run every hour to ensure all my song plays are captured.

`etl.ipynb ` - This script is used to parse the JSON files returned by the API, remove duplicate entries, and load the resulting dataset to a Postgres db from which analysis can be done.

`analysis.ipynb` - This notebook pulls data from the database table previously created and runs some basic data exploration on specific analysis questions.