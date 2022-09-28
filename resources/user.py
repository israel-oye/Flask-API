from flask_restful import Resource, reqparse
from flask import jsonify, make_response

from models.model import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Unique username of new user")
    parser.add_argument('password', type=str, required=True, help="Field cannot be blank")
        
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(username=data["username"]):
            return make_response(jsonify({"message": "Username is taken!"}), 400)
    
        new_user = UserModel(**data)
        new_user.save_to_db()
        return make_response(jsonify({"message": "User created successfully."}), 201)