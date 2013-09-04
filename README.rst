INSTALLATION
============

Download and execute::

    $ python bootstrap.py
    $ bin/buildout

The above commands will download all needed packages and create database with default data loaded from fixtures.

To run application::

    $ bin/django runserver


TASKS OVERVIEW
==============

Medicine test project to complete tasks:
 
# create django project. 

Please use zc.buildout.

# database: 

Hospitals, doctors, patients. Doctors can work in different hospitals. Patients can have multiple doctors. 
Patient (first name, last name, data of birth, contacts, doctors). For data migration please use South.

# views: 

    1) authentication page for patients.
    2) page where pacient can change his profile.
    3) index page lists all hospitals and doctors. Click on doctor shows list of patients(load info via javascript). Add order filters for patients by first name, last name via javascript. 
    4) create one view where superusers(users that have access to admin panel) can add doctors.
    
# create middleware that stores all database requests.

# create signal handler that saves all changes in Patient model

# commands - create django command that prints all patients.

# template-tags - create template tag, that gets any model object, and renders a link of change view in admin interface ( for example: {% edit_list request.user %}).

# forms-widgets - assign calendar widget to "date of birth" field for patient model.

# create template context processor that add django.conf.settings to context.

How-to:
   * create a repo in github
   * commit so frequently as possible. And push your changes at least 1 time per day.
   * type all tasks in Issues, estimate them
   * after completion of every task type real time
   * all tasks should be covered by tests.
 
