import os
import re
import hashlib
from flask import jsonify, url_for
from flask_jwt_simple import create_jwt, jwt_required, get_jwt
from datetime import datetime

class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

# Raises an exception if required params not in body
def check_params(body, *args):
    msg = ''
    if body is None:
        msg = 'request body as a json object, '
    else:
        for prop in args:
            if prop not in body:
                msg += f'{prop}, '
    if msg:
        msg = re.sub(r'(.*),', r'\1 and', msg[:-2])
        raise Exception('You must specify the ' + msg, 400)

def update_table(table, body, ignore=[]):
    ignore = [*ignore, 'id', 'created_at', 'updated_at']
    for attr, value in body.items():
        if attr not in ignore:
            if not hasattr(table, attr):
                raise Exception(f'Incorrect parameter in body: {attr}', 400)
            setattr(table, attr, value)

def sha256(string):
    m = hashlib.sha256()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

def resolve_pagination(request_args, limit_default=10):
    page = request_args.get('page', '0')
    offset = int(page) - 1 if page.isnumeric() and int(page) > 0 else 0
    
    limit = request_args.get('limit', '10')
    limit = int(limit) if limit.isnumeric() and int(limit) > 0 else limit_default
    
    return offset, limit

def resolve_name_day(string):
    a = re.search(r'(.*) - Day ([\d\w]+)', string)
    print('string', string)
    tournament_name = string if a is None else a.group(1)
    flight_day = a and a.group(2)
    print('Tournament Name: ', tournament_name)
    print('Flight Day: ', flight_day)
    return [tournament_name, flight_day]

def are_headers_for(table, file_headers):
    switch = {
        'results': ['Subscriber','Place','Full Name','Winnings','TPS Points','Nationality', 'Event',
            'Residence','User ID','Tournament ID'],
        'casinos': ['SUBSCRIBER','CASINO','STATE (ABB.)','STATE (FULL)','REGION', 'ONLINE',
            'TIME ZONE','ADDRESS','CITY','ZIP CODE','LAT','LONG','WEBSITE'],
        'tournaments': ['Subscriber','Date','Day','Time','Where','Tournament','Buy-in',
            'Starting Stack','Blinds','Structure Link','Casino ID','Multi ID',
            'Tournament ID','H1','NOTES - LOU','Results Link','Entrants']
    }

    for header in switch[table]:
        if header not in file_headers:
            return False
    return True

# Notes: 'admin' will have access even if arg not passed
def role_jwt_required(valid_roles=['invalid']):
    def decorator(func):

        @jwt_required
        def wrapper(*args, **kwargs):

            jwt_role = get_jwt()['role']
            valid = True if jwt_role == 'admin' else False

            for role in valid_roles:
                if role == jwt_role:
                    valid = True

            if not valid:
                raise APIException('Access denied', 403)

            user_id = get_jwt()['sub']
            if not Users.query.get(user_id):
                raise APIException('User not found with id: '+str(user_id), 404)

            kwargs = {
                **kwargs,
                'user_id': user_id
            }

            return func(*args, **kwargs)

        # change wrapper name so it can be used for more than one function
        wrapper.__name__ = func.__name__

        return wrapper
    return decorator
