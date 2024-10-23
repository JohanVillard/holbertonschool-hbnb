import uuid
from datetime import datetime


class Review:
    """Represent a review."""

    def __init__(self, text, rating, user_id, place_id):
        """Initialize an instance of Review class."""
        if not text:
            raise ValueError("Review text is required")
        try:
            rating_int = int(rating)
            if not (1 <= rating_int <= 5):
                raise ValueError
        except ValueError:
            raise ValueError("Rating must be an integer between 1 and 5")

        self.uuid = str(uuid.uuid4())
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, data):
        """Update review."""
        if data["text"] is not None:
            if not data["text"]:
                raise ValueError("Review cannot be empty")
        if data["rating"] is not None:
            try:
                rating_int = int(data["rating"])
                if not (1 <= rating_int <= 5):
                    raise ValueError
            except ValueError:
                raise ValueError("Rating must be an integer between 1 and 5")

        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    # def delete_review(self):

    def __repr__(self):
        return f"<Review id={self.uuid}, rating={self.rating}, \
                    place={self.place.title}, \
                    user={self.user.first_name} {self.user.last_name}>"
