import flask
from utils.red import RQwrap
from utils.mongo import *
import json
import uuid
from datetime import date
red = RQwrap('myq')
red.refreshQueue()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

mongoclient = MongoClient()

@app.route('/', methods=['GET'])
def home():
    return 'Saffron Banking System' 

def get_email_for_token(token):
    cursor = mongoclient.tokens_coll.find_one(({'t':token}))
    if cursor:
        return str(cursor['e'])
    else: 
        return json.dumps({
            'result': 'bad',
            'error_text': 'No token found',
            'error_code': 41
            })

@app.route('/balance', methods=['GET'])
def balance():
    if 'token' in flask.request.args:
    	token = flask.request.args['token']
    else:
    	return json.dumps({
            'result': 'bad',
            'error_text': 'No token found',
            'error_code': 41})  

    email = get_email_for_token(token)

    if not email:
        return json.dumps({
            'result': 'bad',
            'error_text': 'No email found',
            'error_code': 51
            })
    
    print('EMAIL IS ', email)
    data = db_search(email)

    return json.dumps({
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'balance': data['balance']})


def db_search(email):   
    tdct = mongoclient.get_user_data(email)
    return tdct

def db_register(first_name, last_name,email, pword): 
    return mongoclient.add_user(email,first_name,last_name,password=pword)    


@app.route('/register', methods=['GET'])
def register():
    email = None
    pword = None
    fn = None
    ln = None

    if 'email' in flask.request.args:
        email = flask.request.args['email']
    if 'pword' in flask.request.args:
        pword = flask.request.args['pword']
    if 'fn' in flask.request.args:
        fn = flask.request.args['fn']
    if 'ln' in flask.request.args:
        ln = flask.request.args['ln']
    
    if not (email and pword):
        return json.dumps({
            'result': 'bad',
            'error_text': 'Invalid email and password',
            'error_code': 135
            })

    db_res = db_search(email)
    if db_res: #user-ul e deja in db, feel free to modify
        return json.dumps({
            'result': 'bad',
            'error_text': 'Account already is use, you may want to login or recover',
            'error_code': 12
            })

    # print(f'registered email {email} and pass {pword}')  #only for debug, will be removed
    db_register(fn, ln, email, pword)
    return json.dumps({
            'result': 'User added successfully',
            })
@app.route('/generate_token', methods=['GET'])
def generate_login_token():
    email = None
    if 'email' in flask.request.args:
        email = flask.request.args['email'] 
    if not email:
        return json.dumps({
            'result': 'bad',
            'error_text': 'Unable to generate token',
            'error_code': 42
        })
    token = str(uuid.uuid4()) 
    mongoclient.add_token(email,token)
    return "Added token to " + str(email) 

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
    # print('SEARCH IS ',db_res)
    if not db_res:
        return json.dumps({
            'result': 'bad',
            'error_text': 'Email not found',
            'error_code': 23
            })

    if pword != db_res['pword']:
        return json.dumps({
            'result': 'bad',
            'error_text': 'Incorrect password',
            'error_code': 22
            })


    token = generate_login_token()

    return json.dumps({
        'result': 'good',
        'token': token,
        'message': 'Login successfully' 
        })       


@app.route('/transfer', methods=['GET'])
def transfer():
    f = None
    a = None
    t = None

    if 'amm' in flask.request.args:
        f = flask.request.args['from']
        t = flask.request.args['to']
        a = flask.request.args['amm']
        print(f, t, a)
    else:
    	return json.dumps({
        'result': 'bad',
        'error': 'Invalid transfer data',
        'error_code': 33 
        }) 
    
    
    balance = db_search(f)
    if float(balance) < float(a):
        return json.dumps({
            'result': 'bad',
            'error_text': 'Exceeded amount',
            'error_code': 32
            })

    message = {
	'command': 'transfer',
    'source': f,
    'destination': t,
    'amount': a
	}

    mongoclient.add_transaction(f,t,a,date.today())

    red.putMessage(json.dumps(message))
    return 'transfer request sent'


app.run()