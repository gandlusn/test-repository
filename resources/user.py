import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser();

    parser.add_argument('username',type=str,
    required=True
    ,help = "Username field cannot be left blank")
    parser.add_argument('password',type=str,
    required=True
    ,help = "Password field cannot be left blank")

    def post(self):
        data = UserRegister.parser.parse_args();# here UserRegister is class name which is taking in a argument add_resource

        if UserModel.find_by_username(data['username']):
            return {"message":"A user already exists with that username"},400

#        user = UserMode(data['username'],data['password'])
        #or
        user = UserModel(**data)
        user.save_to_db();

        return {"Message": "User created Successfully!!!"}, 201
