import sqlite3

class BotDB:

	def __init__(self, db_file):
		self.conn = sqlite3.connect(db_file)
		self.cursor = self.conn.cursor

	def name(self, name):
		result = self.cursor.execute("INSERT INTO 'some_info' ('name') VALUES(?)", (name,))
		return result.fetchall()