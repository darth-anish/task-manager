# task-manager

Create a board of tasks in a project and assign to different users.

### Features
- Multiple users
- Task creation
- Assignment
- Deadlines
- Status tracking
- Notification for task updates

### Commands to run
1) docker compose run web django-admin startproject task_manager . (to create manage.py and project directory for the django)
2) docker compose up (to run the actual services defined in docker-compose.yml)
3) docker compose run web python manage.py makemigrations && migrate (to make migrations and apply changes in database)
4) docker exec -it task-manager-web-1 /bin/sh (To get inside the web service container) 
