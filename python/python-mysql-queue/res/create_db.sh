#!/bin/bash

set -e 

echo "starting with $0"

user='root'
pass='x'

echo "creating database"
/usr/bin/mysqladmin -u${user} -p${pass} create myqueue
echo "import dump"
/usr/bin/mysql -u${user} -p${pass} myqueue < /vagrant/res/myqueue.sql
echo "done with $0"