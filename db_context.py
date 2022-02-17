import sqlite3

class Sllite3_db_context:
	def __init__(self, connection_string):
		self.connection_string = connection_string

	def execute_query(self, query):
		db = sqlite3.connect(self.connection_string)
		cursor = db.cursor()
		cursor.execute(query)
		db.close()