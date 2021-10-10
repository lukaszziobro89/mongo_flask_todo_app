#!/bin/bash

mongoimport --uri mongodb://mongo_db:27017/todo_db --collection list_of_todos --type json --file /data/init.json --jsonArray