#!/bin/bash
set -eux

# Convenience script for quickly testing changes to model definitions

if [ ! -f manage.py ]
then
  echo "Run script from the root of the Django site"
  exit 1
fi

if [ -f db.sqlite3 ]
then
  rm db.sqlite3
fi

if [ -f projects/migrations/0001_initial.py ]
then
  rm projects/migrations/*py
fi

python manage.py migrate
python manage.py makemigrations projects
python manage.py migrate

python manage.py test

python populate-database.py
