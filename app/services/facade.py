from app.persistence.repository import InMemoryRepository
from app.models.user import User


class HBnBFacade:
    """Represent a facade."""

    def __init__(self):
        """Initiliaze a HBnB facade' instance."""
        self.user_repo = InMemoryRepository()

    def create_user(self, user_data):
        """Create an user."""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Retrieve user's data."""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Retrieve user by mail."""
        return self.user_repo.get_by_attribute("email", email)

    def get_all_users(self):
        """Retrieve all users."""
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        """Update the user's data."""
        self.user_repo.update(user_id, user_data)
        return self.user_repo.get(user_id)
