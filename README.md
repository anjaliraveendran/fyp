# Avian Influenza Surveillance Dashboard
This application is an Avian Influenza Surveillance Dashboard created
using Python-Django backend and PostgreSQL database.
The frontend is developed using an open source bootstrap template for the app layout
and mapping libraries such as MapboxGL.js and Leaflet.js for the GIS functionalities.

###### Prerequisites (for build script)
Ubuntu OS 

## Installation Steps
1. Unzip the downloaded project folder (fyp-master).
2. cd into unzipped folder.
3. Run this command in order to make the shell script executable:
    ```chmod +x gisApp.sh```
4. Now run the shell script:
    ```sudo ./gisApp.sh```
5. Wait for the script to build the entire web app (This might take a while, please wait for the database setup and the dependencies to install correctly)
    <ul>
    <li>The script will promp the user for some inputs - please enter the necessary details. </li>
    <li>PostgreSQL password - you can enter 'password' or any other 1 word you can rememeber</li>
    <li>You will have to re-enter the postgres password</li>
    <li>If installs are going correctly, script will ask you to press 'enter' to continue</li>
    <li>Before loading the data into Postgres and launching the web app, the script will ask the login credentials for the app.
        enter the following:
        username : yourname
        password: yourpassword
        email: youremail
    </li>
    <li>Once this is done the job will load the data into Postgres and set up your web server. Please wait 10-15min as the first load takes a while.</li>
    </ul>
6. Once everything is set up and installed, the terminal will display this:

```Starting development server at http://127.0.0.1:8000/``` <br />
```Quit the server with CONTROL-C.```

Open the link provided in the terminal to access the local webserver.
(Note: Do not click ctrl-C to copy the link as this will exit the terminal and quit the process. Copy the link manually instead.)




