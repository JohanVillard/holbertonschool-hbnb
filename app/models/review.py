import uuid

class Review:
    def __init__(self, comment):
        self.uuid = str(uuid.uuid4())  # Génère un UUID unique
        self.comment = comment

    def __repr__(self):
        return f"<Review uuid={self.uuid}, comment={self.comment}>"
