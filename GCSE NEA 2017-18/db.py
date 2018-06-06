# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute
# https://www.sqlite.org/lang.html

import os
import sqlite3

# connect to database and create cursor
database = 'quiz_data.db'
dir_path = os.path.dirname(os.path.realpath(__file__))
conn = sqlite3.connect(dir_path + '/' + database)
c = conn.cursor()

# create users table
c.execute('''CREATE TABLE IF NOT EXISTS users (
				username TEXT PRIMARY KEY,
				password TEXT NOT NULL,
				name TEXT NOT NULL,
				age INTEGER NOT NULL,
				year_group INTEGER NOT NULL
				)'''
		 )
# create topics table
c.execute('''CREATE TABLE IF NOT EXISTS topics (
				topic_id INTEGER PRIMARY KEY,
				description TEXT UNIQUE NOT NULL
				)'''
		 )
# create difficulties table
c.execute('''CREATE TABLE IF NOT EXISTS difficulties (
				difficulty_id INTEGER PRIMARY KEY,
				description TEXT UNIQUE NOT NULL,
				n_options INTEGER UNIQUE NOT NULL
				)'''
		 )
# create questions table
c.execute('''CREATE TABLE IF NOT EXISTS questions (
				question_id INTEGER PRIMARY KEY,
				topic_id INTEGER NOT NULL,
				question TEXT UNIQUE NOT NULL,
				correct_answer TEXT NOT NULL,
				incorrect_answer01 TEXT NOT NULL,
				incorrect_answer02 TEXT NOT NULL,
				incorrect_answer03 TEXT NOT NULL,
					FOREIGN KEY (topic_id) REFERENCES topics(topic_id)
				)'''
		 )
# create quizzes table
c.execute('''CREATE TABLE IF NOT EXISTS quizzes (
				quiz_id INTEGER PRIMARY KEY,
				username TEXT NOT NULL,
				topic_id INTEGER NOT NULL,
				difficulty_id, INTEGER NOT NULL,
				score INTEGER NOT NULL,
				date DATE NOT NULL,
					FOREIGN KEY (username) REFERENCES users(username),
					FOREIGN KEY (topic_id) REFERENCES topics(topic_id),
					FOREIGN KEY (difficulty_id) REFERENCES difficulties(difficulty_id)
				)'''
		 )

# c.execute("INSERT INTO users VALUES ('testuser', 'password')")

conn.commit()
conn.close()