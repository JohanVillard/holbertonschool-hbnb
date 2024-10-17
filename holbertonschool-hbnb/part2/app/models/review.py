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

    def update_review(self, text=None, rating=None):
        """Update review."""
        if text is not None:
            if not text:
                raise ValueError("Review cannot be empty")
            self.text = text
        if rating is not None:
            try:
                rating_int = int(rating)
                if not (1 <= rating_int <= 5):
                    raise ValueError
                self.rating = rating_int
            except ValueError:
                raise ValueError("Rating must be an integer between 1 and 5")
        self.updated_at = datetime.now()

    # def delete_review(self):

    def __repr__(self):
        return f"<Review id={self.uuid}, rating={self.rating}, \
                    place={self.place.title}, \
                    user={self.user.first_name} {self.user.last_name}>"
