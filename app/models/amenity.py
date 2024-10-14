import uuid
from datetime import datetime

class Amenity:
    def __init__(self, name):

        if not name:
            raise ValueError("Name is required.")

        self.uuid = str(uuid.uuid4())
        self.name= name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_name(self, new_name):
        """Update name"""
        if not new_name:
            raise ValueError("Name is required.")

        self.name = new_name
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"<Amenity id={self.id}, name={self.name}, created_at={self.created_at}, updated_at={self.updated_at}>"
