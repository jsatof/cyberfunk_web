# cyberfunk_web

Cyberfunk is a futuristic-themed rhythm game with rudimentary network capabilities.
This is the Web facing side of cyberfunk. For the game client repository, go here: https://github.com/jsferrarelli/cyberfunk_client


# Demo Video
A run-through of how far we come:
https://www.youtube.com/watch?v=kM1__B-jWEk

# Setup
The web server is deployed on an instance of AWS EC2 virtual machine running Ubuntu 20.04LTS.  

## Tech Stack
- Python 3.8
- Flask web server
- SQLite3 Database

The reason for Python is simplicity, it was a language the team was at least vaguely familliar with. Flask is very straightforwad and quick to get up and running. SQLite was the database of choice solely because the free tier of AWS EC2 provides tiny stotage space. So using the most minimal option would be best.

## Dependencies
Before development can start, the system needs to install some preliminary things from `apt`. Namely:
- gunicorn3
- python3.8
- python3-venv
- sqlite3
- python3-pip

Once those are on your system, run `pip install -r requirements.txt`

# Running
The app is intended to be run with gunicorn with the `start.sh` script. But its still possible to work in a local environment with `python application.py`.
You can send queries via Postmate or cURL. <br><br>
The app is live on https://ec2-3-140-247-200.us-east-2.compute.amazonaws.com (we dont have our own domain)

# Routes
The web app offers delivery of static content, views for datatables, as well as API routes for CRUD operations.
Only 2 routes made it to production:
- `GET /`: Returns index.html with a view of the latest scores uploaded from the game client
- `POST /submit_score`: Inserts the request body into the database

The content of that body looks like this:
```
{
  "username": string,
  "grade": string,
  "score": int,
  "accuracy": float,
  "max_combo", int
}
```

`username` is a string where the player enters their name to associate themselves to the score they obtained. We originally planned to have a login route so we could substitute `username` for `uid` as a foreign key from a User table. But this what we got to for now.<br>
`grade` is a single letter recorded by the game giving a general indicator of how well they did.<br>
`score` is an integer represented the players total accumulated points during their performance.<br>
`accuracy` is a percentage of the notes the player hit over the total number of notes<br>
`max_combo` is counter of their longest streak of notes hit in a row without missing.<br>



