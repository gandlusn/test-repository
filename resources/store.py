from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_my_name(name)
        if store:
            return store.json();
        return {'Message':'store Not FOUND !!!'}, 404

    def post(self,name):
        if StoreModel.find_my_name(name):
            return {'Message':'Store already Exists'}, 400
        store = StoreModel(name);
        store.save_to_db();
        return {'Message':'store CREATED'}, 200

    def delete(self,name):
        if StoreModel.find_my_name(name):
            store = StoreModel.find_my_name(name);
            store.delete_from_db();
        return {'Message':'store Deleted'}
class StoreList(Resource):

    def get(self):
        return {'STORES':[ store.json() for store in StoreModel.query.all()]}
