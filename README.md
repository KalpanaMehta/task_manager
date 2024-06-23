<<<<<<< HEAD
Task Management Application

This is a Task Management Application built with Django and Django REST Framework for the back-end and HTML,CSS, Js, Bootstrap for the front-end. The application allows users to create, view, update, and delete tasks. Each task includes a title, description, due date, and status (Pending, Started, or Completed).

Features
Landing page displaying a list of tasks
Add new tasks with a title, description,status and due date
View detailed information of each task
Edit existing tasks
Delete tasks
Responsive design for both desktop and mobile devices
Task status indication (Pending, Started, Completed)

Technologies Used
Django
Django REST Framework
Bootstrap
HTML
CSS
JavaScript

Installation
Clone the repository:
git clone https://github.com/your-username/task-management-app.git
cd task-manager
Create a virtual environment and activate it:
python -m venv venv
`venv\Scripts\activate`

Run the migrations:
python manage.py migrate

Create a superuser:
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Access the application in your web browser:

Navigate to http://127.0.0.1:8000/

Usage
Add Task: Click the "Add Task" button on the landing page to create a new task.
View Task: Click on a task title to view its details.
Edit Task: Click the "Edit" button  to update its details.
Delete Task: Click the "Delete" button next to remove it from the list.

Project Structure

task_management_app/
│
├── tasks/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   ├── templates/
│   │   ├── tasks/
│   │   │   ├── base.html
│   │   │   ├── index.html
│   │   │   ├── task_detail.html
│   │   │   ├── task_form.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── task_manageer/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── manage.py
CSS Styling
The custom styles for the application are defined in the styles.css file located in the tasks/static/css/ directory. The file includes styles for the title, buttons, task status badges, and overall layout.


Acknowledgments
Django
Django REST Framework
Bootstrap
=======
Task Management Application

This is a Task Management Application built with Django and Django REST Framework for the back-end and HTML,CSS, Js, Bootstrap for the front-end. The application allows users to create, view, update, and delete tasks. Each task includes a title, description, due date, and status (Pending, Started, or Completed).

Features
Landing page displaying a list of tasks
Add new tasks with a title, description,status and due date
View detailed information of each task
Edit existing tasks
Delete tasks
Responsive design for both desktop and mobile devices
Task status indication (Pending, Started, Completed)

Technologies Used
Django
Django REST Framework
Bootstrap
HTML
CSS
JavaScript

Installation
Clone the repository:
git clone https://github.com/KalpanaMehta/task_manager.git
cd task-manager
Create a virtual environment and activate it:
python -m venv venv
`venv\Scripts\activate`

Run the migrations:
python manage.py migrate

Create a superuser:
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Access the application in your web browser:

Navigate to http://127.0.0.1:8000/

Usage
Add Task: Click the "Add Task" button on the landing page to create a new task.
View Task: Click on a task title to view its details.
Edit Task: Click the "Edit" button  to update its details.
Delete Task: Click the "Delete" button next to remove it from the list.


CSS Styling
The custom styles for the application are defined in the styles.css file located in the tasks/static/css/ directory. The file includes styles for the title, buttons, task status badges, and overall layout.


Acknowledgments
Django
Django REST Framework
Bootstrap
>>>>>>> 06d39d25723f04cf740e539adb0737b78db8bb1e
