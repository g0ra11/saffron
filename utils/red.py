from rsmq import RedisSMQ
import redis

class RQwrap():

    rq = None

    def __init__(self, queue_name="saffron_queue", ack_time=20):
        redis_client = redis.Redis(host="SG-SapphronRedis-34689.servers.mongodirector.com", port=6379, password="PCPYqZOTpc1KpU3yqtYfkKAKpkQQGN4j")

        self._qname = queue_name
        self._ack = ack_time

        self._q = RedisSMQ(qname=self._qname, client=redis_client)

    def createQueue(self):
        self._q.createQueue(qname=self._qname, vt=self._ack).execute()

    def refreshQueue(self):
        self._q.deleteQueue(qname=self._qname).exceptions(False).execute()
        self._q.createQueue(qname=self._qname, vt=self._ack).execute()

    def putMessage(self, message):
        return self._q.sendMessage(qname=self._qname).message(message).execute()

    def getMessage(self):
        return self._q.receiveMessage(qname=self._qname).execute()

    def ackMessage(self, message_id):
        return self._q.deleteMessage(qname=self._qname, id=message_id).execute()

