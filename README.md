README
======

Things you need to do first to run this webapp
----------------------------------------------

You need to create ``virtual environment`` for Python:

	$ python -m venv venv

Activate your ``venv``:

	$ cmd: venv\Scripts\activate
	----------------------------

	$ powershell: .venv\Scripts\activate
	------------------------------------
	
	$ git: source venv\Scripts\activate
	-----------------------------------

Install ``django`` and ``mysqlclient``:

	$ pip install django
	--------------------

	$ pip install mysqlclient
	-------------------------

Make migrations:

	$ python manage.py makemigrations
	--------------------------------
	
	$ python manage.py migrate
	--------------------------





 
