from app.persistence.repository import InMemoryRepository
from app.models.user import User
from datetime import datetime


class HBnBFacade:
    """Represent a facade."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        """Override __new__ to control instance creation (Singleton)."""
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """Initiliaze a instance of class HBnBFacade."""
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
        user = self.user_repo.get(user_id)
        if user is None:
            return None
        
        update_data = {}
        if "first_name" in user_data:
            update_data["first_name"] = user_data["first_name"]
        if "last_name" in user_data:
            update_data["last_name"] = user_data["last_name"]
        if "email" in user_data:
            update_data["email"] = user_data["email"]
        
        self.user_repo.update(user_id, update_data)
        return self.user_repo.get(user_id)