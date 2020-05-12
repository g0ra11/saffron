from utils.red import RQwrap
import json
import time

red = RQwrap('myq')

def process(command):
	
	com = json.loads(command)

	if com['command'] == 'transfer':

		print(f'I transfered {com["ammount"]} from {com["source"]} to {com["destination"]}')

while 1:
	try:
		message = red.getMessage()
		process(message['message'])
		red.ackMessage(message['id'])

	except:
		time.sleep(1)



