This application is an Avian Influenza Surveillance Dashboard created
using Python-Django backend and PostgreSQL database.
The frontend is developed using an open source bootstrap template for the app layout
and mapping libraries such as MapboxGL.js and Leaflet.js for the GIS functionalities.
<!-- This application is built  -->
<!-- and tested for python version 3.6. -->

How to install:
cd Downloads/fyp-master/
sudo apt-get install python3-distutils
python3 get-pip.py
python3 -m pip install virtualenv
sudo apt-get install python3-venv
python3 -m venv myenv


sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update

sudo apt-get install postgresql-11
sudo apt-get install postgis postgresql-11-postgis-3-scripts

sudo passwd postgres
<enter new password>
su - postgres
<enter password>

psql
<<< inside postgres >>
CREATE USER sample_user WITH PASSWORD 'sample_password';
CREATE DATABASE avianinfluenza WITH OWNER sample_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO sample_user;
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
ALTER ROLE sample_user SUPERUSER;
<<< >>>


. myenv/bin/activate
pip install wheel
pip install psycopg2-binary
sudo apt install python3.6-dev
sudo apt-get install libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev

pip install -r requirements.txt

## GDAL
sudo add-apt-repository ppa:ubuntugis/ppa
sudo apt-get update
sudo apt-get install gdal-bin

sudo apt-get install libgdal-dev
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal
pip install GDAL==2.4.2


<<< Issues with leaflet - deleted the folder for it from lib and then did
pip install leaflet
>>>

python3 manage.py makemigrations landingpage

PYTHONPATH=/path/to/django/parent/dir
python3 manage.py createsuperuser
python3 manage.py migrate
python manage.py runserver --noreload

(login with superuser credentials)





