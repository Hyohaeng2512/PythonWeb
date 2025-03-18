import firebase_admin
from firebase_admin import credentials, auth

if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://pythonweb-aa728-default-rtdb.asia-southeast1.firebasedatabase.app"
    })


def register_user(email, password):
    return auth.create_user(email=email, password=password)

def login_user(email, password):
    user = auth.get_user_by_email(email)
    return user.uid