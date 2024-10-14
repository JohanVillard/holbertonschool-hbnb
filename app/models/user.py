import uuid
from datetime import datetime

class User:
    def __init__(self, first_name, last_name, email, is_admin=false):

        if not first_name:
            raise ValueError("First name is required.")

        if not last_name:
            raise ValueError("Last name is required.")

        if not email:
            raise ValueError("Email is required.")

        self.uuid = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_user(self, new_first_name=None, new_last_name=None, new_email=None):
        """Update user"""

        if not any([new_first_name, new_last_name, new_email]):
            raise ValueError("Need to change at least one value.")

        if new_first_name:
            self.first_name = new_first_name

        if new_last_name:
            self.last_name = new_last_name

        if new_email:
            self.email = new_email

        self.updated_at = datetime.now()

    def __repr__(self):
        return f"<User uuid={self.uuid}, name={self.first_name} {self.last_name}, email={self.email}, is_admin={self.is_admin}, created_at={self.created_at}, updated_at={self.updated_at}>"
