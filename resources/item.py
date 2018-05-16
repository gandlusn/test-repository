from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser();

    parser.add_argument('price',type=float,
    required=True
    ,help = "This field cannot be left blank")
    parser.add_argument('store_id',type=int,
    required=True
    ,help = "Every Items needs a Stoer id");

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_my_name(name)

        if item:
            return item.json();
        else:
            return{'Message':"item Not found"},404

    def post(self,name):

            # here force=True converts any type of format request in to json format
        if ItemModel.find_my_name(name):
            return {'message': 'An item with name {} already exists'.format(name)}, 400 # user mistake
        data =  Item.parser.parse_args();
        item = ItemModel(name,**data)
        print(item.json())
        try:
            item.save_to_db()
        except:
            return {'message':'An Error Occurred while Inserting'}, 500 # internal server error
        return item.json(), 201


    def delete(self,name):
        item = ItemModel.find_my_name(name);

        if item:
            item.delete_from_db();
        return {'message':'Item Delted'}


    def put(self,name):

        data =  Item.parser.parse_args();
        item = ItemModel.find_my_name(name)


        if item is None:

            item = ItemModel(name,data['price'],data['store_id']);

        else:

            item.price = data['price'];

        item.save_to_db();

        return item.json();


class ItemList(Resource):
    def get(self):
        return {'items':list(map(lambda x:x.json(),ItemModel.query.all()))}
