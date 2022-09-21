from resources.user import UserModel
import hmac

def authenticate(username, pwd):
    user = UserModel.find_by_username(username=username)

    if user and hmac.compare_digest(user.password, pwd):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id=user_id)



