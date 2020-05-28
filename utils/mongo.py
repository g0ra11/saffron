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

    def add_user(self, email, first_name, last_name, password, api_token=None):
        user_doc = dict(_id=email, fn=first_name, ln=last_name, p=password, t=api_token, m=0, b=0)
        try:
            self.users_coll.insert_one(user_doc)
        except err.DuplicateKeyError:
            raise UserAlreadyExistsError("Users exists")

    def add_transaction(self, sender, reciever, amount, date):
        trans_doc = dict(s=sender, r=reciever, a=amount, d=date)
        self.transactions_coll.insert_one(trans_doc)

    def add_token(self, email, token):
        token_doc = dict(e=email, t=token)
        try:
            self.tokens_coll.insert_one(token_doc)
        except err.DuplicateKeyError:
            raise TokenExistsError("Token exists")

    def get_all_token_for_user(self, email):
        cursor = self.tokens_coll.find({"e": email})
        token_list = []
        for doc in cursor:
            token_list.append(doc.get('t'))
        return token_list

    def get_user_data(self, email):
        doc = self.users_coll.find_one({"_id": email})
        if not doc:
            return None
        return User(doc)


class User:
    def __init__(self, doc):
        self.email = doc.get("email")
        self.first_name = doc.get("fn")
        self.last_name = doc.get("ln")
        self.hash = doc.get("p")
        self.balance = doc.get("m")
        self.blocked = doc.get("b")
