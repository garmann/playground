#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='testing argparse...')
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

if args.type == 'create':
	print('create')
elif args.type == 'update':
	print('update')
elif args.type == 'finish':
	print('finish')
else:
	print('shit happens')