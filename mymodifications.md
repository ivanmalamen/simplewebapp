# I had to adjust the following:

## *requirements.txt*
In order to use the *mariadb* I had to add the library in the requirements.txt: 'Flask-MySQLdb'

## create dockerfile

### dockerfile
why did I integrate the following code:
`--no-cache`
`--no-cache-dir`
In order to keep the Docker image size small, I prevent the two package managers from storing local copies of the package database index file.

**In some situations this is of course a disadvantage, especially if build speed is more important than size. such as ci/cd or the cloud**

## command from Readme.md 
*** point 1 ***
The command is intended for *Debian-based Linux* distributions, but we use *"alpine Linux"*

## port
in the *app.py* the port was 8080, but in the *readme.md* the port 5000 is specified for the Dockerfile, 
so I had to decide which one to change, 
I decided to change the *dockerfile* and the *app.py* to adapt to the readme and now use port **5000**.

## start mariaDB
docker run --name mariadb -e MYSQL_ROOT_PASSWORD=myrootpassword -e MYSQL_DATABASE=mydatabase -e MYSQL_USER=chris -e MYSQL_PASSWORD=mypassword -p 3307:3307 -d mariadb:latest


## adjust the app.py
- Additional imports
- Database connection configuration
- Initialization of MySQL
- New route
- Port change

---

# how to use:
1.  open a terminal an write the code to start mariadb:
    `docker run --name mariadb -e MYSQL_ROOT_PASSWORD=myrootpassword -e MYSQL_DATABASE=mydatabase -e MYSQL_USER=chris -e MYSQL_PASSWORD=mypassword -p 3307:3307 -d mariadb:latest`
2. write the following code to build the flask app:
    `docker build -t my-flask-app .`
3. write the following code to run the flask app:
    `docker run -p 5000:5000 --name flask-app -e MYSQL_PORT=3307 --link mariadb:mysql -d my-flask-app`

***# Current error ***
I can't access the mariadb yet, I'll continue working soon
