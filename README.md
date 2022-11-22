# distributed-systems-cw/
Linux instructions!

Installing the code
    Please git clone the repository or extract the files from zip
    You should have 3 folders: adam-API, client and hamzah-API

activate venv on 3 different terminals
    source .venv/bin/activate

ensure 'export FLASK_APP=run.py' and 'export FLASK_ENV=development' are in your bashrc file

cd into client and run client on port 8000
    flask run --port=8000

cd into hamzah-API and run hamzah-API on port 8001
    flask run --port=8001

cd into adam-API and run adam-API on port 8002
    flask run --port=8002

client will be at localhost:8000 in the browser

Enter a country from 'England', Germany' or 'Spain' to search for the league in that country
You will see a page stating the league name and a list of all teams currently in the league
Choose a team and you will receive a page detailing information about that team
