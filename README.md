#### multiuser logging webapp with flask
____
Project Directories
* proximalog/   `the application code and files.`
* tests/        `test modules.`
* venv/         `virtual environment for Flask and other dependencies.`


Setup and Activate Virtual Environment
* python3 -m venv venv
* . venv/bin/activate

Update pip and install flask
* pip install -U pip
* pip install flask

Initialized the database
* flask init-db

Tell Flask where to find the application and running it in development mode.
* export FLASK_APP=proximalog
* export FLASK_ENV=development
