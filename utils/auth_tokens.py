import redis
import random
import string


def generate_token(stringLength):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letters_and_digits) for i in range(stringLength)))


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

    def get_auth_token(self, email):
        token = generate_token(15)
        self._insert_auth_token(token, email)
        return token
