#!/usr/bin/env python3

from classes.myqueue import MyQueue
import time # time.sleep(0.02)
import random # random.randint(1, 100)
import socket # socket.gethostname()
import sys
import argparse

CONF_DB = {
			'server': 'localhost',
			'user': 'root',
			'pass': 'x',
			'db': 'myqueue'
			}

def worker_create(q, amount):
	# makes objects in state new
	hostname = socket.gethostname()
	while amount > 0:
		amount -= 1
		objectname = "{}_{}_{}".format(hostname, int(time.time()), random.randint(1,10000000))
		q.object_add(objectname)

		
def worker_update(q, amount):
	# changes objects into status running
	while amount > 0:
		amount -= 1
		try:
			objectid = q.object_get_object_bystate('new')[0]['object']
			q.object_update_status(name=objectid, status='running')
		except IndexError: # happens when there are no new objects
			pass


def worker_finish(q, amount):
	# changes objects into status done
	while amount > 0:
		amount -= 1
		try: 
			objectid = q.object_get_object_bystate('running')[0]['object']
			q.object_update_status(name=objectid, status='done')
		except IndexError: # happens when there are no running objects
			pass


def main(args):
	q = MyQueue(CONF_DB)
	with q:
		# using "with" ensures db exit, not worked on my testing with the db library
		# see __enter__ & __exit__ in MyQueue Class

		if args.type == 'create':
			worker_create(q, args.amount)
		elif args.type == 'update':
			worker_update(q, args.amount)
		elif args.type == 'finish':
			worker_finish(q, args.amount)
		else:
			print('shit happens')
			sys.exit(1)

	# mysql> select status, count(object) as count from queue group by status order by count DESC
	# set global general_log = 'ON';


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='its me, the python queue...')
	parser.add_argument('type', 
		default='create', 
		help='for type: choose between create, update and finish',
		choices=['create', 'update', 'finish'],
		type=str)
	parser.add_argument('--amount',
		type=int,
		default=1000,
		help='amount to create/modify/finish')

	args = parser.parse_args()

	main(args)
