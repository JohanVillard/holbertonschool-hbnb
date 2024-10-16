import uuid
from datetime import datetime


class Place:
    """Represent an place."""

    def __init__(self, title, price, latitude, longitude, owner, description=None):
        """Initialize an Place's instance."""
        self.is_valid_length(title, 1, 100)

        self.uuid = str(uuid.uuid4())
        self.title = title
        self.price = float(price)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.owner = owner
        self.description = description
        self.reviews = []  # List of reviews of this instance
        self.amenities = []  # List of amenities of the instance
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0 or not isinstance(value, float):
            raise ValueError("The price must be positive")
        self.__price = value

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if not -90 <= value <= 90 or not isinstance(value, float):
            raise ValueError("Latitude must be between -90 and 90")
        self.__latitude = value

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if not -180 <= value <= 180 or not isinstance(value, float):
            raise ValueError("Latitude must be between -180 and 180")
        self.__longitude = value

    def update_place(
        self, new_title, price, latitude, longitude, owner, new_description=None
    ):
        """Update place."""
        self.is_valid_length(new_title, 1, 100)

        self.title = new_title
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.description = new_description

        self.updated_at = datetime.now()

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add a review to the place."""
        self.amenities.append(amenity)

    def is_valid_length(self, input, min, max):
        """Check the length of the input."""
        if not (min <= len(input) <= max) or input is None:
            raise ValueError(f"{input} be between {min} and {max} characters.")
