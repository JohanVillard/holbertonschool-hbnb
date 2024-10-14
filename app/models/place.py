import uuid

class Place:
    def __init__(self, name):
        self.uuid = str(uuid.uuid4())  # Génère un UUID unique
        self.name = name

    def __repr__(self):
        return f"<Place uuid={self.uuid}, name={self.name}>"
