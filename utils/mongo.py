import pymongo
import pymongo.errors as err
from datetime import datetime

MONGO_URL = "mongodb://admin:2qPY5KhDlqBUbS3b@sapphronmongo-shard-00-00-ntfay.gcp.mongodb.net:27017,sapphronmongo-shard-00-01-ntfay.gcp.mongodb.net:27017,sapphronmongo-shard-00-02-ntfay.gcp.mongodb.net:27017/test?ssl=true&replicaSet=SapphronMongo-shard-0&authSource=admin&w=majority"


class UserAlreadyExistsError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class TokenExistsError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class MongoClient:
    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_URL)
        self.database = self.client.get_database("sapphron")
        self.tokens_coll = self.database.get_collection("tokens")
        self.users_coll = self.database.get_collection("users")
        self.transactions_coll = self.database.get_collection("transactions")

    def add_user(self, email, password, api_token=None):
        user_doc = dict(_id=email, p=password, t=api_token, m=0, b=0)
        try:
            self.users_coll.insert_one(user_doc)
        except err.DuplicateKeyError:
            raise UserAlreadyExistsError("Users exists")

    def add_transaction(self, sender, receiver, amount, date):
        trans_doc = dict(s=sender, r=receiver, a=amount, d=date)
        self.transactions_coll.insert_one(trans_doc)

    def add_token(self, email, token, amount, reciever):
        created = datetime.utcnow()
        token_doc = dict(e=email, t=token, a=amount, r=reciever, c=created)
        try:
            self.tokens_coll.insert_one(token_doc)
        except err.DuplicateKeyError:
            raise TokenExistsError("Token exists")

    def get_all_token_for_user(self, email):
        cursor = self.tokens_coll.find({"e": email})
        token_list = []
        for doc in cursor:
            token_list.append({
                'paykey': doc.get('t'),
                'email': doc.get('r'),
                'amount': doc.get('a')
            })
        return token_list

    def get_token_data(self, token):
        token = self.tokens_coll.find_one({"t": token})
        return token

    def delete_token(self, token):
        self.tokens_coll.remove({'t': token})

    def get_user_data(self, email):
        doc = self.users_coll.find_one({"_id": email})
        if not doc:
            return None
        return User(doc).__repr__()

    def modify_balance(self, email, amount):
        result = self.users_coll.update_one({'_id': email}, {'$inc': {'m': amount}})
        return result

    def modify_blocked(self, email, amount):
        result = self.users_coll.update_one({'_id': email}, {'$inc': {'b': amount}})
        return result

    def modify_balance_and_set_blocked(self, email, amount):
        result = self.users_coll.update_one({'_id': email}, {'$inc': {'m': -amount, 'b': amount}})



class User:
    def __init__(self, doc):
        self.email = doc.get("email")
        self.hash = doc.get("p")
        self.balance = doc.get("m")
        self.blocked = doc.get("b")

    def __repr__(self):
        return {'email': self.email, 'pword': self.hash, 'balance': self.balance, 'block': self.blocked}