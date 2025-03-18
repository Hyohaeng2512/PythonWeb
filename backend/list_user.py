import firebase_admin
from firebase_admin import auth, credentials

# Load serviceAccountKey.json (Tải từ Firebase Console)
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Lấy danh sách user
def list_users():
    users = auth.list_users().iterate_all()
    for user in users:
        print(f"UID: {user.uid}, Email: {user.email}, Created At: {user.user_metadata.creation_timestamp}")

# Gọi hàm
list_users()
