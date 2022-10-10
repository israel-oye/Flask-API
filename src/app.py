from datetime import timedelta
import os
from dotenv import load_dotenv
from .security import authenticate, identity
from .db import db, migrate
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


app = Flask(__name__)
api = Api(app)

load_dotenv()
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=1)

jwt = JWT(app, authenticate, identity)
db.init_app(app)
migrate.init_app(app, db)

with app.app_context():
    db.create_all()

api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    
    app.run(debug=True)