import sqlite3

# Naming database file
db_file = 'QuizBowlDatabase.db'

# Connect to the database (this will create a new file if it doesn't exist)
conn = sqlite3.connect(db_file)

# Close the connection
conn.close()

print(f"Database file '{db_file}' created successfully.")
