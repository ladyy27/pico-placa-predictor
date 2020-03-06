# pico-placa-predictor
A predictor app to determine if a vehicle can be on road according its license plate and a date and a time (Based in the Pico&amp;Placa past rules) [Check it here](https://ecuador.seguros123.com/todo-lo-que-debes-saber-del-famoso-pico-y-placa/)

**NOTE:** These steps were written for Mac OS, Other OS are supported from the virtual environment creation 

## Requirements
**Server** 
- Python 3.7
- Django 3.0.3
- Django REST 3.11.0
- SQLite
- Pip3 (python3 get-pip.py)
- Virtualenv (pip install virtualenv)

**Client** 
- Node.js Version 10.14.2
- Angular 8: 0.803.24

**TDD TOOL: ** [unittest](https://docs.python.org/3/library/unittest.html#module-unittest)

## How to run the project

**How run the Server**
1. Choose a directory to create the virtual environment **predictorenv**:
	```sh
	#Create a virtual environment & activate it
	$ virtualenv predictorenv
	$ source predictorenv/bin/activate
	```
2. In **pico_placa_predictor** directory, install all specified tools  in **requirements.txt** file
	```sh
	$ pip install -r requirements.txt
	```
3. Go to **pico_placa_predictor** directory and run the following commands in order to create all Django models (classes) in the default database SQLite :
	```sh
	$ python manage.py migrate
	$ python manage.py makemigrations pico_placa
	$ python manage.py migrate
	```
4. Run the server with :
	```sh
	$ python manage.py runserver
	```
5. Type Ctrl-C to down the server. 
6. The performed tests are in reservationapp/tests.py. To see the result of the tests, run: 
	```sh
	$ python manage.py test
	```

7. To deactivate hotelReservationenv from any path, run:
	```sh
	$ deactivate
	```
**How run the Client**
 1. From the **picoPlacaPredictorClient** directory, run:
	```sh
	$ npm install
	$ ng serve 
	```
	By default, the client ups in 4200 port: http://localhost:4200/

## How the predictor works

The predictor app is Client-Server model. The server is an API REST (Django REST) and the Client is performed by Angular.
In the form, enter:
1. A License plate (which format is 3 letters & 4 numbers, i.e. 'ABC1234')
2. A Date and Time
3. Submit

It will show you if a car with that license plate can or not can be on the road at that date and that time. If the license plate format is not correct, the predictor notifies you.
