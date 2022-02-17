import sqlite3

try:
	db = sqlite3.connect('server.db')
	cursor = db.cursor()
	# name = 'Ignat'

	cursor.execute("INSERT INTO 'some_info' ('name') VALUES (?)", ('Igor111',))

	name = cursor.execute("SELECT * FROM 'some_info'")
	# print(some_info.fetchall())

	db.commit()

except sqlite3.Error as error:
	print('Error', error)

finally:
	if(db):
		db.close

