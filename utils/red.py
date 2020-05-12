from rsmq import RedisSMQ


class RQwrap():

	rq = None

	def __init__(self, queue_name, host='localhost', ack_time=20):

		self._qname = queue_name
		self._host = host
		self._ack = ack_time

		self._q = RedisSMQ(qname=self._qname, host=self._host)

	def refreshQueue(self):
		self._q.deleteQueue(qname=self._qname).exceptions(False).execute()
		self._q.createQueue(qname=self._qname, vt=self._ack).execute()


	def putMessage(self, message):
		return self._q.sendMessage(qname=self._qname).message(message).execute()

	def getMessage(self):
		return self._q.receiveMessage(qname=self._qname).execute()

	def ackMessage(self, message_id):
		return self._q.deleteMessage(qname=self._qname, id=message_id).execute()

