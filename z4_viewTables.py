import sqlite3

def view_all_data(database_file):
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

        # Execute a SELECT query to fetch all data
        cursor.execute("SELECT * FROM your_table_name")  # Replace 'your_table_name' with the actual table name

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print the column headers
        col_names = [description[0] for description in cursor.description]
        print("\t".join(col_names))

        # Print the data
        for row in rows:
            print("\t".join(str(value) for value in row))

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    finally:
        # Close the database connection
        if connection:
            connection.close()

# Replace 'your_database_file.db' with the actual database file name
view_all_data('QuizBowlDatabase.db')
