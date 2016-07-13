from classes.dbcon import dbcon

class MyQueue():
	def __init__(self, CONF_DB):
		self.db = dbcon(CONF_DB)

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.db.close()

	def __enter__(self):
		return self

	def object_list(self):
		sql = "SELECT object FROM queue"
		return(self.db.get(sql))

	def object_add(self, name, status='new'):
		sql = "INSERT INTO queue (object, status) VALUES ('{}', '{}')".format(name, status)
		self.db.set(sql)

	def object_del(self, name):
		sql = "DELETE FROM queue WHERE object = '{}'".format(name)
		self.db.set(sql)

	def object_update_status(self, status, name):
		sql = "UPDATE queue SET status = '{}' WHERE object = '{}'".format(status, name)
		self.db.set(sql)

	def object_get_object_bystate(self, status= None):
		sql = "select object from queue where status = '{}' limit 1".format(status)
		return(self.db.get(sql))



