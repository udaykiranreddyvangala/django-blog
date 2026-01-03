DJANGO BLOG APPLICATION
=======================

Live Website:
-------------
https://udaydjangoblogs.pythonanywhere.com/

GitHub Repository:
------------------
https://github.com/udaykiranreddyvangala/django-blog


PROJECT DESCRIPTION
-------------------
This is a Django-based blog web application that allows users to create, view,
and manage blog posts with image uploads. The project demonstrates core Django
concepts such as models, views, templates, authentication, media handling, and
deployment on PythonAnywhere.

The application is suitable for learning Django fundamentals as well as for use
as a base project for more advanced features.


FEATURES
--------
- User authentication (login & logout)
- Create, update, and delete blog posts
- Upload and display images with posts
- Admin panel for managing posts and users
- Media file handling for uploaded images
- Clean UI using Django templates
- Deployed and publicly accessible on PythonAnywhere


TECHNOLOGIES USED
-----------------
- Python 3
- Django Framework
- SQLite Database
- HTML, CSS
- Django Admin
- PythonAnywhere (Deployment)


PROJECT STRUCTURE
-----------------
django-blog/
│
├── blog/                  # Blog application
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS)
├── media/                 # Uploaded media files
├── db.sqlite3             # Database
├── manage.py              # Django management file
├── requirements.txt       # Project dependencies
└── README.txt             # Project documentation


SETUP INSTRUCTIONS (LOCAL)
--------------------------

1. Clone the repository:
   git clone https://github.com/udaykiranreddyvangala/django-blog.git

2. Navigate to the project directory:
   cd django-blog

3. Create a virtual environment:
   python3 -m venv venv

4. Activate the virtual environment:
   Linux / macOS / WSL:
   source venv/bin/activate

   Windows:
   venv\Scripts\activate

5. Install dependencies:
   pip install -r requirements.txt

6. Apply database migrations:
   python manage.py makemigrations
   python manage.py migrate

7. Create a superuser:
   python manage.py createsuperuser

8. Run the development server:
   python manage.py runserver

9. Open in browser:
   http://127.0.0.1:8000/


MEDIA FILE CONFIGURATION
------------------------
The project uses Django's media handling for image uploads.

settings.py configuration:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

For production deployment (PythonAnywhere), media files are served using
manual URL mapping in the Web → Static files section.


DEPLOYMENT
----------
The project is deployed on PythonAnywhere.

Live URL:
https://udaydjangoblogs.pythonanywhere.com/

Deployment steps include:
- Setting DEBUG = False
- Configuring ALLOWED_HOSTS
- Mapping /static/ and /media/ directories
- Reloading the web app from PythonAnywhere dashboard


AUTHOR
------
Name: Vangala Uday Kiran Reddy  
GitHub: https://github.com/udaykiranreddyvangala  

This project was built for learning and demonstrating Django web development.


LICENSE
-------
This project is open-source and free to use for educational purposes.
