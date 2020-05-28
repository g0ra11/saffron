from utils.red import RQwrap
import json
import time
from utils.mongo import MongoClient


red = RQwrap('myq')
mongoclient = MongoClient()


def process(command):
	
	com = json.loads(command)

	if com['command'] == 'transfer':

		print(f'I transfered {com["amount"]} from {com["source"]} to {com["destination"]}')
		mongoclient.modify_blocked(command['source'],float(command["a"]))
		mongoclient.modify_balance(command['source'],-float(command["a"] ))
		mongoclient.modify_balance(command['destination'],float(command["a"] ))
		
		
while 1:
	try:
		message = red.getMessage()
		process(message['message'])
		red.ackMessage(message['id'])

	except:
		time.sleep(1)



