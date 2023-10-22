# LTItestproject
Here is a step by step procedure for LTI Django project and run:
I am using pycharm to run the application.
step 1: Install pycharm and python  if not installed
step 2: follow these commands 
django-admin startproject ProjectName (to create a project)
python ./manage.py startapp AppName (to create app)
python ./manage.py migrate AppName (to apply migration changes)
Python manage.py runserver(to verify Django server project working or not)
pip install django-sslserver (to install sslserver in windows)
step 3: after installing sslserver follow the below command
python ./manage.py runsslserver 127.0.0.1:8000
step4: Then a link is generated with the local host and click it to open in a new window.
step5: now modify the link by https://127.0.0.1:8000/lti/
now your LTI Application has successfully executed with an output
output: Welcome to Computer Science Education
