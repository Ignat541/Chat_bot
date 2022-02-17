
class UserRepository:
		
	def __init__(self, db_context):
		self.db_context = db_context

	def add_user (self, user):
		add_query = "INSERT INTO 'some_info' ('name') VALUES (?)", user.first_name
		self.db_context.execute_query(add_query)

	def update_user(self, user):
		update_query = "update some_info set name=(?) where some_info.id=(?)", user.first_name, user.id
		self.db_context.execute_query(update_query)