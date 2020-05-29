import redis
import uuid


class AuthManager:
    def __init__(self):
        self.redis_client = redis.Redis(host="SG-SapphronRedis-34689.servers.mongodirector.com", port=6379,
                                        password="PCPYqZOTpc1KpU3yqtYfkKAKpkQQGN4j", db=2)

    def get_email_for_token(self, token):
        email = self.redis_client.get(token)
        if email:
            return email.decode('utf-8')
        return None

    def delete_auth_token(self, token):
        self.redis_client.delete(token)

    def _insert_auth_token(self, token, email):
        self.redis_client.set(token, email)

    @staticmethod
    def _create_token():
        token = uuid.uuid4()
        return str(token)

    def get_auth_token(self, email):
        token = self._create_token()
        self._insert_auth_token(token, email)
        return token
