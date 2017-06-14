# blackboard
Verteilte Systeme Testat

To try a live demo, visit our [GitHub page](https://manfredvonteichman-tit14.github.io/blackboard/).

## What is 'blackboard'?

A RESTful web service offering the functionality to create, read, write to and delete a blackboard. (CRUD)
Furthermore it offers to clear the blackboard message and querying the blackboard status. To find out more,
visit the [wiki](https://github.com/manfredvonteichman-tit14/blackboard/wiki/Task-description).

## Getting Started

### Installation
To get the server up and running, the following steps must be followed. 

* Following requirements must be installed:
  - [Python 3.6.x](https://www.python.org/downloads/) (or latest)
  - pip (should be installed automatically with Python)
* Following requirements can be installed (dev):
  - virtualenv (install by executing `pip install virtualenv`)
* Clone this GitHub repository:
  - `git clone https://github.com/manfredvonteichman-tit14/blackboard`
* (optional | dev) Setup virtual environment:
  * Install virtualenv with `pip install virtualenv`
  * Create virtualenv with `virtualenv -p python3 venv`
  * Activate virtualenv
      - Linux / macOS specific activation: `source venv/bin/activate`
      - Window specific activation: `venv\bin\activate`
  * To deactivate the virtual environment use: `deactivate`
* Install the requirements with pip:
  - `pip install -r requirements.txt`
* Set the PYTHONPATH:
  - Linux / macOS: `export PYTHONPATH="."`
  - Windows: `set PYTHONPATH=.`

### Running the web service

Start the server by running: `python blackboard_api\blackboard_server.py` on Windows and respectiveley `python blackboard_api/blackboard_server.py` on Linux/macOS
By default the server listens on all interfaces and can therefore be reached at
`http://127.0.0.1:1337/api/v1`
