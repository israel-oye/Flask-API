from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask import make_response
from models.model import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name",
        type=str,
        required=True,
        help="Name cannot be blank."
    )

    def get(self, name):
        data = Store.parser.parse_args()
        store = StoreModel.find_by_name(name=data["name"])
        if store:
            return make_response(store.json(), 200)
        return make_response({"message": "Store not found."}, 404)

    @jwt_required()
    def post(self, name):
        data = Store.parser.parse_args()

        if StoreModel.find_by_name(data["name"]):
            return make_response({"message": f"Item with name: {data['name']} exists!"}, 400)
        new_store = StoreModel(name=data["name"])
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
            return make_response({'message': 'Store deleted'}, 200)
        return make_response({'message': 'Store not found'}, 400)


class StoreList(Resource):
    def get(self):
        return make_response({"stores": [store.json() for store in StoreModel.query.all()]}, 200)