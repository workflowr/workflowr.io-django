#!/bin/bash
set -eux

# Convenience script for quickly testing changes to model definitions

rm db.sqlite3
rm projects/migrations/*py

python manage.py migrate
python manage.py makemigrations projects
python manage.py migrate

python manage.py test
