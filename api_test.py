import flask
from utils.red import RQwrap
import json

red = RQwrap('myq')
red.refreshQueue()

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "This resource is not here"

def get_email_for_token(token):
    if token == 'fuck':
        return 'ion@maria.com'
    else:
        return None

@app.route('/balance', methods=['GET'])
def balance():
    if 'token' in flask.request.args:
    	token = flask.request.args['token']
    else:
    	return 'no user provided'

    email = get_email_for_token(token)

    if not email:
        return json.dumps({'error_text': 'You have been logged out', 'error_code': 15, 'result': 'bad'})

    data = db_search({'email': email})

    return json.dumps({'balance': data['balance'], 'result': 'good'})




def db_search(data):  #Dummy 
    tdct = {'email': 'ion@maria.com', 'pword': 'mere', 'balance': 100}
    return tdct

def db_register(email, pword):  #Dummy
    return True     


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
            'error_text': 'Invalid request type',
            'error_code': 20
            })

    db_res = db_search({'email': email})

    if db_res: #user-ul e deja in db, feel free to modify
        return json.dumps({
            'result': 'bad',
            'error_text': 'Account already is use, you may want to login or recover',
            'error_code': 21
            })

    print(f'registered email {email} and pass {pword}')  #only for debug, will be removed
    db_register(email, pword)
    return json.dumps({
            'result': 'good',
            })

def generate_login_token():
    return 'fuck'

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
            'error_text': 'Invalid request type',
            'error_code': 30
            })

    db_res = db_search({'email': email})

    if not db_res:
        return json.dumps({
            'result': 'bad',
            'error_text': 'Account not found',
            'error_code': 31
            })

    if pword != db_res['pword']:
        return json.dumps({
            'result': 'bad',
            'error_text': 'Wrong password',
            'error_code': 32
            })


    token = generate_login_token()

    return json.dumps({'token': token, 'result': 'good'})       


@app.route('/transfer', methods=['GET'])
def transfer():
	if 'amm' in flask.request.args:
		f = flask.request.args['from']
		t = flask.request.args['to']
		a = flask.request.args['amm']

		print(f, t, a)
	else:
		return 'not good request'

	message = {
	'command': 'transfer',
	'source': f,
	'destination': t,
	'ammount': a
	}

	red.putMessage(json.dumps(message))
	return 'request sent'

app.run()