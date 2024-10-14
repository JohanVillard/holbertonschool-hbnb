import uuid
from datetime import datetime

class Place:
    def __init__(self, title, description, price, latitude, longitude, owner):

        if not title:
            raise ValueError("Title is required.")

        if not description:
            raise ValueError("Description is required.")

        if not isinstance(price, float) or price <= 0:
            raise ValueError("Price must be a float greter than 0.")

        if not isinstance(latitude, float) or not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be a float between -90.0 and 90.0.")
        
        if not isinstance(longitude, float) or not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be a float between -180.0 and 180.0.")

        self.uuid = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_place(self, title=None, description=None, price=None, latitude=None, longitude=None):
        """Update place"""
        if title is not None:
            if not title:
                raise ValueError("Title cannot be empty.")
            self.title = title
        if description is not None:
            if not description:
                raise ValueError("Description cannot be empty.")
            self.description = description
        if price is not None:
            if not isinstance(price, float) or price <= 0:
                raise ValueError("Price must be a float greater than 0.")
            self.price = price
        if latitude is not None:
            if not isinstance(latitude, float) or not (-90.0 <= latitude <= 90.0):
                raise ValueError("Latitude must be a float between -90.0 and 90.0.")
            self.latitude = latitude
        if longitude is not None:
            if not isinstance(longitude, float) or not (-180.0 <= longitude <= 180.0):
                raise ValueError("Longitude must be a float between -180.0 and 180.0.")
            self.longitude = longitude
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"<Place uuid={self.uuid}, owner={self.owner.first_name} {self.owner.last_name}, price={self.price}, latitude={self.latitude}, longitude={self.longitude} created_at={self.created_at}, updated_at={self.updated_at}>"
