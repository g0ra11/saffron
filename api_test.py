import flask
from utils.red import RQwrap
from utils.mongo import *
import json
import hashlib
import random
import string

red = RQwrap('myq')
red.refreshQueue()

app = flask.Flask(__name__)
app.config["DEBUG"] = True
mongoclient = MongoClient()


@app.route('/', methods=['GET'])
def home():
    return 'Saffron Banking System' 


def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



def get_email_for_token(token):
    return 'adaj@yahoo.com'


@app.route('/balance', methods=['GET'])
def balance():

    if 'token' in flask.request.args:
        token = flask.request.args['token']
    else:
        return json.dumps({
            'result': 'bad',
            'error_text': 'Malformed request',
            'error_code': 41})  

    email = get_email_for_token(token)

    if not email:
        return json.dumps({
            'result': 'bad',
            'error_text': 'You have been logged out',
            'error_code': 51
            })

    data = db_search(email)

    if not data:
        return json.dumps({
            'result': 'bad',
            'error_text': 'Something went wrong',
            'error_code': 51
            })

    return json.dumps({
        'result': 'good',
        'balance': data['balance']})


def db_search(email):
    try:
        tdct = mongoclient.get_user_data(email)
    except Exception:
        return None

    return tdct


@app.route('/register', methods=['GET'])
def register():
    email = None
    pword = None

    if 'email' in flask.request.args:
        email = flask.request.args['email']
    if 'pword' in flask.request.args:
        pword = flask.request.args['pword']

    if not (email and pword):
        return json.dumps({
            'result': 'bad',
            'error_text': 'Invalid email and password',
            'error_code': 135
            })

    enc_pass = hashlib.sha256(pword.encode('utf-8')).hexdigest()

    try:
        mongoclient.add_user(email, password=enc_pass)
    except UserAlreadyExistsError:
        return json.dumps({
                'result': 'bad',
                'error_text': 'Account already is use, you may want to login or recover',
                'error_code': 12
                })
    except:
        return json.dumps({
                'result': 'bad',
                'error_text': 'Something went wrong',
                'error_code': 12
                })

    return json.dumps({'result': 'good'})


@app.route('/request_money_token', methods=['GET'])
def request_money_token():
    email = None
    amount = None
    user = None

    if 'email' in flask.request.args:
        email = flask.request.args['email']
    if 'amount' in flask.request.args:
        amount = flask.request.args['amount']
    if 'user' in flask.request.args:
        user = flask.request.args['user']

    if not (email and amount and user):
        return json.dumps({
            'result': 'bad',
            'error_text': 'invalid request',
            'error_code': 42
        })

    paykey = randomString()

    try:
        amount = int(amount)
    except ValueError:
        return json.dumps({
            'result': 'bad',
            'error': 'Invalid request',
            'error_code': 33
            })

    if amount < 0:
        return json.dumps({
            'result': 'bad',
            'error': 'Invalid request',
            'error_code': 33
            })

    mongoclient.add_token(user, paykey, amount, email)
    return json.dumps({
        'result': 'good',
        'mesage': 'paykey generated ok'
    })


@app.route('/get_my_paykeys', methods=['GET'])
def get_my_paykeys():
    token = None

    if 'token' in flask.request.args:
        token = flask.request.args['token']

    if not token:
        return json.dumps({
            'result': 'bad',
            'error': 'Invalid request data',
            'error_code': 33
            })

    email = get_email_for_token(token)

    if not email:
        return json.dumps({
            'result': 'bad',
            'error': 'You have been logged out',
            'error_code': 33
            })

    paykeys = []

    try:
        paykeys = mongoclient.get_all_token_for_user(email)
    except:
        return json.dumps({
            'result': 'bad',
            'error': 'Something went wrong',
            'error_code': 33
            })

    return json.dumps({
        'result': 'good',
        'paykeys': paykeys
    })


@app.route('/redeem_paykey', methods=['GET'])
def redeem_paykey():
    paykey = None

    if 'paykey' in flask.request.args:
        paykey = flask.request.args['paykey']

    if not paykey:
        return json.dumps({
            'result': 'bad',
            'error': 'Invalid request',
            'error_code': 33
            })

    paykey_data = mongoclient.get_token_data(paykey)

    if not paykey_data:
        return json.dumps({
            'result': 'bad',
            'error': 'Invalid token',
            'error_code': 33
            })

    message = {
        'command': 'transfer',
        'source': paykey_data['e'],
        'destination': paykey_data['r'],
        'amount': paykey_data['a']
        }

    mongoclient.modify_balance(paykey_data['e'], -paykey_data['a'])
    mongoclient.modify_blocked(paykey_data['e'], paykey_data['a'])

    mongoclient.delete_token(paykey)
    red.putMessage(json.dumps(message))
    return json.dumps({
        'result': 'good',
        'message': 'request sent'
    })



@app.route('/login', methods=['GET'])
def login():
    email = None
    pword = None

    if 'email' in flask.request.args:
        email = flask.request.args['email']
    if 'pword' in flask.request.args:
        pword = flask.request.args['pword']

    if not (email and pword):
        return json.dumps({
            'result': 'bad',
            'error_text': 'Incorrect email and password',
            'error_code': 232
            })

    db_res = db_search(email)

    if not db_res:
        return json.dumps({
            'result': 'bad',
            'error_text': 'Email not found',
            'error_code': 23
            })

    enc_pass = hashlib.sha256(pword.encode('utf-8')).hexdigest()

    if enc_pass != db_res['pword']:
        return json.dumps({
            'result': 'bad',
            'error_text': 'Incorrect password',
            'error_code': 22
            })

    token = 'fuck'  # DAJ , de adaugat auth token in redis

    return json.dumps({
        'result': 'good',
        'token': token,
        'message': 'Login successfully' 
        })       


@app.route('/transfer', methods=['GET'])
def transfer():
    token = None
    amount = None
    to = None

    if 'token' in flask.request.args:
        token = flask.request.args['token']
    if 'amm' in flask.request.args:
        amount = flask.request.args['amm']
    if 'to' in flask.request.args:
        to = flask.request.args['to']

    if not (token and amount and to):
        return json.dumps({
            'result': 'bad',
            'error': 'Invalid transfer data',
            'error_code': 33
            })

    try:
        amount = int(amount)
    except ValueError:
        return json.dumps({
            'result': 'bad',
            'error': 'Invalid request',
            'error_code': 33
            })

    if amount < 0:
        return json.dumps({
            'result': 'bad',
            'error': 'Invalid request',
            'error_code': 33
            })

    email = get_email_for_token(token)  # DAJ, de bagat auth token
    data = db_search(email)
    bal = data['balance']

    if bal < amount:
        return json.dumps({
            'result': 'bad',
            'error_text': 'Not enough money',
            'error_code': 32
            })

    message = {
        'command': 'transfer',
        'source': email,
        'destination': to,
        'amount': amount
        }

    mongoclient.modify_balance(email, -amount)
    mongoclient.modify_blocked(email, amount)

    red.putMessage(json.dumps(message))
    return json.dumps({
        'result': 'good',
        'message': 'request sent'
    })


app.run()
