import uuid

class User:
    def __init__(self, username):
        self.uuid = str(uuid.uuid4())  # Génère un UUID unique
        self.username = username

    def __repr__(self):
        return f"<User uuid={self.uuid}, username={self.username}>"
