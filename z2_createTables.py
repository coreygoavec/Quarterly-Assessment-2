import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('QuizBowlDatabase.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define SQL command to create a table to hold questions for Entrepreneurship
cursor.execute('''CREATE TABLE IF NOT EXISTS Entrepreneurship (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    option1 TEXT,
                    option2 TEXT,
                    option3 TEXT,
                    option4 TEXT,
                    correct_answer TEXT
                )''')

# Define SQL command to create a table to hold questions for Business Applications Development
cursor.execute('''CREATE TABLE IF NOT EXISTS BusinessApplicationsDevelopment (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    option1 TEXT,
                    option2 TEXT,
                    option3 TEXT,
                    option4 TEXT,
                    correct_answer TEXT
                )''')

# Define SQL command to create a table to hold questions for Organizational Leadership
cursor.execute('''CREATE TABLE IF NOT EXISTS OrganizationalLeadership (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    option1 TEXT,
                    option2 TEXT,
                    option3 TEXT,
                    option4 TEXT,
                    correct_answer TEXT
                )''')

# Define SQL command to create a table to hold questions for Business Intelligence and Analytics Capstone
cursor.execute('''CREATE TABLE IF NOT EXISTS AnalyticsCapstone (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    option1 TEXT,
                    option2 TEXT,
                    option3 TEXT,
                    option4 TEXT,
                    correct_answer TEXT
                )''')

# Define SQL command to create a table to hold questions for Business Strategy
cursor.execute('''CREATE TABLE IF NOT EXISTS BusinessStrategy (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    option1 TEXT,
                    option2 TEXT,
                    option3 TEXT,
                    option4 TEXT,
                    correct_answer TEXT
                )''')