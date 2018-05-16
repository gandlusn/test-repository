from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password==password:#if user is true and user.password==password that is retreived from database then it will authenticate and send token
        return user;

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)# same happens here as that happens i authentication
