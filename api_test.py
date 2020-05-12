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


@app.route('/balance', methods=['GET'])
def balance():
    if 'user' in flask.request.args:
    	user = flask.request.args['user']
    else:
    	return 'no user provided'

    return f'balance for {user} is {1000}'


@app.route('/transfer', methods=['GET'])
def trabsfer():
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