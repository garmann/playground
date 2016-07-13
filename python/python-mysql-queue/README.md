# content

this is a simple play with python3 and mysql to build a queue.

## python code
run this app with: python app.py

- app.py is the entry point
- classes/myqueue.py maps the meta db functions
 - object_list: list objects in db
 - object_add: adds objects into db
 - object_del: deletes objects from db
 - object_update_status: updates objects from db
 - see main() for example calls
- classes/dbcon.py
 - makes the plain db connection

## os or vagrant config
i used it with my setup vagrant box, just change the base image. you have to install the pip requirements. i suggest to use virtualenv.

- pip3 install -r requirements.txt