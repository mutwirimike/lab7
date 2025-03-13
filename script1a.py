import pandas as pd
import sqlite3
from pprint import pprint

# Opens a connection to an SQLite database.
con = sqlite3.connect('bond_movies.db')
cur = con.cursor()

# Define an SQL query that creates a table named 'movies'.
create_bond_table_query = """ CREATE TABLE IF NOT EXISTS movies (
                        Year INTEGER,
                        Movie TEXT,
                        Bond TEXT,
                        Avg_User_IMDB REAL)
                        """

# Corrected the add_movie_query syntax
add_movie_query = """ INSERT INTO movies
                       (Year, Movie, Bond, Avg_User_IMDB)
                       VALUES (?, ?, ?, ?);"""  # Added closing parenthesis and corrected the syntax

# Corrected the new_movie tuple syntax
new_movie = (2027, 
              'Bond by Amazon',
              'TBD',
              0.0)  # Changed '0' to 0.0 to match the REAL type

# Execute the SQL query to create the 'movies' table.
cur.execute(create_bond_table_query)

# Read the CSV file into a DataFrame
bond_df = pd.read_csv('jamesbond.csv')
print(bond_df.head())

# Insert each row from the DataFrame into the database
for row in bond_df.itertuples(index=False):
    cur.execute('''INSERT INTO movies (Year, Movie, Bond, Avg_User_IMDB)
                   VALUES (?, ?, ?, ?)''', (row.Year, row.Movie, row.Bond, row.Avg_User_IMDB))

# Execute the add_movie_query to insert the new movie
cur.execute(add_movie_query, new_movie)

# Fetch all movies from the database
cur.execute('SELECT * FROM movies')
all_movies = cur.fetchall()

# Pretty print the results
pprint(all_movies)

# Commit (save) pending transactions to the database.
con.commit()

# Close the database connection.
con.close()

# Read the movies from the database into a DataFrame and print it
# Note: You need to reopen the connection to read from the database again
con = sqlite3.connect('bond_movies.db')
print(pd.read_sql_query('SELECT * FROM movies', con))

# Close the connection again
con.close()