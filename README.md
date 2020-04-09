This application is an Avian Influenza Surveillance Dashboard created
using Python-Django backend and PostgreSQL database.
The frontend is developed using an open source bootstrap template for the app layout
and mapping libraries such as MapboxGL.js and Leaflet.js for the GIS functionalities.
<!-- This application is built  -->
<!-- and tested for python version 3.6. -->

How to install:

1. Install python 3.7 on your PC.
2. Download application source code from github:
3. Open the project in any IDE (PyCharm is preferred)
<!-- 4. Setup project interpreter (setup python venv) and project structure. -->
<!--    - In PyCharm follow below steps -->
<!--      - PyCharm -> Preferences -> Project -> Project Interpreter -->
<!--      ![Alt text](scrrenshots/PyCharm1.png?raw=true "Setup Project Interpreter PyCharm") -->
<!--      - PyCharm -> Preferences -> Project -> Project Structure -->
<!--      ![Alt text](scrrenshots/PyCharm2.png?raw=true "Setup Project Structure PyCharm") -->
5. In the settings.py file, configure database details:
    "ndlcncn"

6. The following 2 commands will set up the db with appropriate tables of our "landingpage" django app:
    Run on terminal:

   <django-env>/python manage.py makemigrations landingpage
   <django-env>/python manage.py migrate

7. To create an admin user for the application, run:

   <django-env>/python manage.py createsuperuser

   and set admin username and password of your choice.

8. Finally, run the application using this command:

   <django-env>/python manage.py runserver --noreload

9. Now open http://localhost:8000/ on your browser to see the app in action

10. To populate the db tables with our Avian Influenza outbreak data, go to landingpage -> admin.py
    scroll down to line 182 to this line of code:

    class EmpresDomesticWildHumanAdmin(LeafletGeoAdmin):

    and un-comment the code under it. (This code populates the db with our datasets)




