# Quizston

[Quiz Website](http://hakob.pythonanywhere.com) - Know how much clever you are.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Installation

Quizston requires [Python](https://www.python.org/) v3+ to run (preferable Python 3.6).

Install the dependencies and devDependencies and start the server.

```sh
$ sudo apt install python3-pip
$ pip3 install virtualenv
$ cd ~ && git clone https://github.com/Hakob/Quizston.git
$ cd Quizston
$ virtualenv --python=python3.6 venv 
$ source venv/bin/activate
(venv)$ pip3 install -r requirements.txt 
(venv)$ python manage.py runserver
```

## Pre Deployment actions
Last command will install Django framework with third-part libs and drivers with it, especially mysqlclient requires *_libmysqlclient-dev_* package for Linux OS

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
