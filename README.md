# About

This class project is a miniature E-commerce web application built on top of a distributed database using Django, MongoDB and Docker. 

## How to use?
You need to initialize the back-end and front-end servers first on your machine 

### Back-end Initialization

1- Make sure you have Docker and MongoDB installed on you machine

2- make sure localhost:7000 is not occuppied by any other application

3- Run `cd Backend/app`

4- Then run `docker-compose up -d --build`

5- Open mongo-compass

6- Make a new conection to default port

7- Create a new database

8- Provide the new database info in `settings.py`

9- Run `docker-compose exec app python manage.py migrate`


### Front-end Initialization

1- Run `cd Frontend`

2- Run `npm install or yarn`

3- Run `npm start or yarn start`
