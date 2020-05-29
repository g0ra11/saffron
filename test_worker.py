from utils.red import RQwrap
import json
import time
from utils.mongo import MongoClient


red = RQwrap('myq')
mongoclient = MongoClient()


def process(command):
	
	command = json.loads(command)
	print('received', command)

	if command['command'] == 'transfer':
		data = mongoclient.get_user_data(command['destination'])


		if not data:
			mongoclient.modify_blocked(command['source'], -command['amount'])
			mongoclient.modify_balance(command['source'], command['amount'])
			return

		mongoclient.modify_blocked(command['source'], -command['amount'])
		mongoclient.modify_balance(command['destination'], command['amount'])
		mongoclient.add_transaction(command['source'], command['destination'], command['amount'], int(time.time()))


while 1:
	try:
		message = red.getMessage()
		process(message['message'])
		red.ackMessage(message['id'])
	except Exception as e:
		print(e)
		time.sleep(1)



