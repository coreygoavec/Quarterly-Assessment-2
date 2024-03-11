import sqlite3

# Assuming you have a dictionary with questions and answers
questions_and_answers = {
    "Question 1": "Answer 1",
    "Question 2": "Answer 2",
    "Question 3": "Answer 3",
    # Add more questions and answers as needed
}

# Specify your SQLite database file path
db_file_path = 'QuizBowlDatabase.db'

# Establish a connection to the database
connection = sqlite3.connect(db_file_path)

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Assuming your table is named 'your_table_name' with columns 'question' and 'answer'
table_name = 'your_table_name'

# Create the table if it doesn't exist
create_table_query = f'''
CREATE TABLE IF NOT EXISTS {table_name} (
    question TEXT,
    answer TEXT
);
'''
cursor.execute(create_table_query)

# Populate the table with data from the dictionary
for question, answer in questions_and_answers.items():
    insert_data_query = f'''
    INSERT INTO {table_name} (question, answer)
    VALUES (?, ?);
    '''
    cursor.execute(insert_data_query, (question, answer))

# Commit the changes and close the connection
connection.commit()
connection.close()
