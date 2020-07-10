# Restaurant API
Manage and store client orders with a RESTful API created with Flask and Flask-RESTful.
## Requirements
- **Python 3.x**
- **MySQL**
### Test API
To run the api for testing, you need to follow these steps:
1. Install MySQL on your computer (I used [XAMPP](https://www.apachefriends.org/es/index.html))
2. In the project folder `db/` has **SQL** scripts that creates database schema and example data (sorry I had lazy to translate to *English*):
    - `schema.sql`: you can run this script in **phpMyAdmin** (if you installed *XAMPP* obviously) or directly in console
    - `products.csv`: data to import to **Product** table
    - `data.sql`: *INSERT queries* to store example data. To access MySQL console in a terminal, you can use this command:
    ```
    $ mysql -h hostname -u username -p userpassword
    ```
3. Create a configuration file (I usually name it `config.ini`), with the following key values:
```
[SERVER_CONFIG]
api_version=Actual version
appname=Flask name app
port=Server port
[MYSQL_DATA]
host=Hostname of MySQL
user=User to access database
password=Password (if not required leave if empty)
database=Database to use
```
4. *[Optional]* Create a virtual enviroment for this project.
5. Install modules specified in `requirements.txt`, if use a virtual enviroment this command would help you:
```
(venv) $ pip install -r requirements.txt
```
6. Run the file `api.py`:
```
(venv) $ python src/api.py
```
#### Notes
- *The instruction LOAD DATA INFILE doesn't work well on phpMyAdmin so I recommend to run it directly in console.*
- Image files are stored in the server disk, you only **register the path** where is located the images.
- **Make sure to specify or check the code are reading the configuration file correctly, I run the project from the root folder.**
- API uses in some resources authentication made with **Flask-HTTPAuth**, the type is *Basic Auth*, you need to set header `Authorization` with `username` and `password`.
##### Version 0.2.0
