import uuid
from datetime import datetime


class Review:
    """Represent a review."""

    def __init__(self, text, rating, place, user):
        """Initialize an instance of Review class."""
        if not text:
            raise ValueError("Review text is required")
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")

        self.id = str(uuid.uuid4())
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_review(self, text=None, rating=None):
        """Update review."""
        if text is not None or not text:
            raise ValueError("Review cannot be empty")
            self.text = text
        if rating is not None:
            if not isinstance(rating, int) or not (1 <= rating <= 5):
                raise ValueError("Rating must be an integer between 1 and 5")
            self.rating = rating
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"<Review id={self.id}, rating={self.rating}, \
                    place={self.place.title}, \
                    user={self.user.first_name} {self.user.last_name}>"
