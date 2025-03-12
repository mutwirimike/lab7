import sqlite3
# Opens a connection to an SQLite database.
# Returns a Connection object that represents the database connection.
# A new database file will be created if it doesn't already exist.
con = sqlite3.connect('bond_movies.db')
# Get a Cursor object that can be used to run SQL queries on the database.
cur = con.cursor()
# Define an SQL query that creates a table named ‘movies’.
# Each row in this table will hold information about a specific movie.
create_bond_table_query = """ CREATE TABLE IF NOT EXISTS movies (
                        Year INTEGER,
                        Movie TEXT,
                        Bond TEXT,
                        Avg_User_IMDB REAL)
                        """
# Execute the SQL query to create the ‘movies’ table.
# Database operations like this are called transactions.
cur.execute(create_bond_table_query)
# Commit (save) pending transactions to the database.
# Transactions must be committed to be persistent.
con.commit()
# Close the database connection.
# Pending transactions are not implicitly committed, so any
# pending transactions that have not been committed will be lost.
con.close()

print()