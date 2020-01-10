#!/bin/bash
set -eux

# Create a temporary superuser for testing the site

python manage.py createsuperuser \
  --username admin \
  --email admin@example.com \
