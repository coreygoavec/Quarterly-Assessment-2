import sqlite3

def create_table():
    # Connect to the SQLite database (replace 'your_database.db' with your actual database file)
    conn = sqlite3.connect('QuizBowlDatabase.db')
    cursor = conn.cursor()

    # Get table name from user
    table_name = input("Enter the name for the table: ")

    # Get the number of columns for the table
    num_columns = int(input("Enter the number of columns for the table: "))

    # Initialize an empty list to store column definitions
    columns = []

    # Prompt the user to enter column names and types
    for i in range(num_columns):
        column_name = input(f"Enter the name for column {i + 1}: ")
        column_type = input(f"Enter the type for column {i + 1} (e.g., TEXT, INTEGER): ")
        columns.append(f"{column_name} {column_type}")

    # Create the SQL query to create the table
    create_table_query = f"CREATE TABLE {table_name} ({', '.join(columns)});"

    # Execute the query to create the table
    try:
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the function to create the table
create_table()
