from db import db

class UserModel(db.Model):
    '''User model class '''
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        
    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    # store = db.relationship("StoreModel")

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    
    def json(self):
        try:
            return {
                "name": self.name,
                "price": self.price,
                "store": self.store.name
            }
        except AttributeError:
            return  {
                "name": self.name,
                "price": self.price,
                "store": None
            }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    items = db.relationship("ItemModel", lazy='dynamic', backref='store')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            "store id": self.id,
            "name": self.name,
            "items": [item.json() for item in self.items.all()]
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()






