from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.model import ItemModel
from models.model import StoreModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type=float,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument(
        "name",
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument(
        "store_id",
        type=int,
        required=True,
        help="Every item needs a store id"
    )
   

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return make_response(item.json(), 200)
        return make_response(jsonify({'message': 'Item not found'}), 404)

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return make_response(jsonify({'message': 'Item with that name already exists!'}), 400)

        data = Item.parser.parse_args()
        
        new_item = ItemModel(data["name"], data["price"], data["store_id"])
        try:
            new_item.save_to_db()
        except:
            return make_response(jsonify({"message": "An error occured with insertion"}), 500)
        
        return make_response(new_item.json(), 201)
    
    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return make_response(jsonify({"message": f"Item '{name}' deleted successfully."}), 200)
        return make_response(jsonify({"message": f"Item '{name}' not found"}, 404))
    
    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(data["name"])

        if item is None:
            item = ItemModel(**data)
        else:
            item.price = data["price"]
            item.store_id = data["store_id"]

        item.save_to_db()
        return make_response(item.json())

class ItemList(Resource):

    def get(self):
        store_items = [{"name": item.name, "price": item.price} for item in ItemModel.query.all()]
        return make_response(jsonify({"items": store_items}), 200)