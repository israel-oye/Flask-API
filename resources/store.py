from flask_restful import Resource
from flask_jwt import jwt_required
from flask import make_response
from models.model import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return make_response(store.json(), 200)
        return make_response({"message": "Store not found."}, 404)

    def post(self, name):
        if StoreModel.find_by_name():
            return make_response({"message": f"Item with name: {name} exists!"}, 400)
        new_store = StoreModel(name=name)
        try:
            new_store.save_to_db()
        except:
            return make_response({'message': 'An error occured while creating store...Try again.'}, 500)
        else:
            return make_response(new_store.json(), 200)

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()


class StoreList(Resource):
    def get(self):
        return [store.json() for store in StoreModel.query.all()]