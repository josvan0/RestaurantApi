# RestaurantApi
Manage and store client orders with a RESTful API created with Flask and Flask-RESTful and use authentication with Flask-HTTPAuth.

## Requirements
- **Python 3.x**
- **MySQL**

### Test API
To run the api for testing, you need to follow the next steps:
1. Install MySQL on your computer (I used [XAMPP](https://www.apachefriends.org/es/index.html) for development)
2. In the project folder `db/` has **SQL** scripts files that creates database schema and create example data (sorry I had lazy to translate to *English*)
    - `schema.sql`: you can run this file in **phpMyAdmin** (if you installed *XAMPP* obviously)
    - `products.csv`: data to import to **Product** table
    - `data.sql`: *INSERT queries* to store example data. ***Note: The instruction LOAD DATA doesn't work well on phpMyAdmin** so I recommend to run it **directly in console**. To access MySQL console in a terminal, you can use this command:
    ```
    $ mysql -h hostname -u username -p userpassword
    ```
3. In root project create a configuration file (I usually use `config.ini`), with the following key values:
```
[SERVER_CONFIG]
api_version=Indicates actual version
appname=Name Flask app
port=Port of server
[MYSQL_DATA]
host=Hostname of MySQL
user=User to access database
password=Password (if not required leave if empty)
database=Database to use
```
4. [Optional] Create a virtual enviroment for this project.
5. Install modules specified in `requirements.txt`, if use a virtual enviroment this command would help you:
```
(venv) $ pip install -r requirements.txt
```
6. Access to **folder project** and from here run the file `api.py`:
```
(venv) $ python src/api.py
```
***Note: If you run it from other directory, make sure to specify or check the code are reading the configuration file.**

#### Version 0.1.0
