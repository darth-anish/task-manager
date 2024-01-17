#!/bin/bash

# Check if the project is already initialized
if [ ! -f /app/manage.py ]; then
  # If not initialized, run the startproject command
  django-admin startproject myproject .
  python manage.py migrate
fi

# Start the Django development server
python manage.py runserver 0.0.0.0:8000