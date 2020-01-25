# from flask_sqlalchemy import SQLAlchemy
from models import db, Users, Casinos, Tournaments, Flights, Results, Subscribers
from datetime import datetime, timedelta
from utils import sha256


def run_seeds():

    Results.query.delete()
    Flights.query.delete()
    Tournaments.query.delete()
    Users.query.delete()
    Subscribers.query.delete()

    db.session.execute("ALTER SEQUENCE users_id_seq RESTART")
    db.session.execute("ALTER SEQUENCE tournaments_id_seq RESTART")
    db.session.execute("ALTER SEQUENCE flights_id_seq RESTART")
    db.session.execute("ALTER SEQUENCE results_id_seq RESTART")
    db.session.execute("ALTER SEQUENCE subscribers_id_seq RESTART")

    
    c1 = Casinos(
        name = 'Seminole Hard Rock Hollywood',
        address = '1234 SW 57 Ave',
        city = 'Hollywood',
        state = 'FL',
        zip_code = '',
        longitude = 0,
        latitude = 0,
        website = '',
        h1 = ''
    )

    t1 = Tournaments(
        casino = c1,
        name = 'Hard Rock Night $400 Guaranteed',
        buy_in = '',
        blinds = 0,
        starting_stack = 0,
        results_link = '',
        structure_link = '',
        start_at = datetime.strptime('1-Dec-19 9:00 AM', '%d-%b-%y %I:%M %p'),
        notes = ''
    )
    db.session.add_all([c1, t1])

    db.session.add( Subscribers(
        company_name = 'Swap Profit',
        api_host = 'http://localhost:3000',
        api_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTU4MTM1NTIsImlhdCI6MTU3OTgxMzU1MiwibmJmIjoxNTc5ODEzNTUyLCJzdWIiOjEsInJvbGUiOiJhZG1pbiJ9.1_rMYxvQtp2KiCGreT5frEMUApDh_hPx3322OZiiVa0"
    ))
    
    db.session.commit()