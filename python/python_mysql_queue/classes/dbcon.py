import pymysql.cursors
import sys

class dbcon():
	def __init__(self, CONF_DB):
		self.connection = pymysql.connect(
			host=CONF_DB['server'],
			user=CONF_DB['user'],
			password=CONF_DB['pass'],
			db=CONF_DB['db'],
			charset='utf8',
			cursorclass=pymysql.cursors.DictCursor
			)

	def get(self, sql):
		try:
			with self.connection.cursor() as c:
				c.execute(sql)
				result=c.fetchall()
				return(result)
		finally:
			pass

	def set(self, sql):
		try:
			with self.connection.cursor() as c:
				c.execute(sql)
		except pymysql.err.IntegrityError:
			#place for rollback or else
			print('could not change data, object may already exists')
			#sys.exit(1)			

		self.connection.commit()

	def close(self):
		self.connection.close()