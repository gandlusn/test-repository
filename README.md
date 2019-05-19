This is a Python Flask Appliction that contains three models in it, Users, Stores, Items, a User can be entitled to one or more than one
store and store will have one or more items in it.

I used flask_jwt library to create a Tokenis for authetication and have a /auth endpoint to request for a Token, with correct username and passsword.

This application uses SQLALCHEMY as its's ORM to create tables and query data from them. 

This API is compatible to run on cloud, for that you need to install requirements.txt and store
the database information in the Environmental varibles

To run this app you need to run the commans: python app.py(in that folder).

The 5 Endpoints of the API are.

1. /ItemList: This returns all the items in all the stores
2. /item/<string:name>: This will return one particular and its details like price etc
3. /register: This is used to create a new user and get token
4. /store/<string:name>: This will return the store and all the items it contains
5. /stores: This will return all the stores.
