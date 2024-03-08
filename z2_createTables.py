import sqlite3

# Establishing connection to databse file
conn = sqlite3.connect("QuizBowlDatabase.db")
cr = conn.cursor()

# Creating new tables
cr.execute()