import os
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate, identity
from resources.user import UserRegister;
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///..\data.db');# either one of this.
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
app.secret_key='jose';
items= [{"name":"chair","price":15.99}];


jwt = JWT(app,authenticate,identity) #/auth: we send it user name and password


api.add_resource(ItemList,"/Items")
api.add_resource(Item,'/item/<string:name>')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')



if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True);
