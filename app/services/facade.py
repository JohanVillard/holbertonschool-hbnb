from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review


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
        self.place_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        # self.association_repo = InMemoryRepository()

    # ----------------------------------------------------------- #
    ##########################_USER_###############################
    # ----------------------------------------------------------- #
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

        user.update_user(
            new_first_name=user_data.get("first_name"),
            new_last_name=user_data.get("last_name"),
            new_email=user_data.get("email"),
        )
        self.user_repo.update(user_id, user.__dict__)
        return user

    # ----------------------------------------------------------- #
    ##########################_PLACE_##############################
    # ----------------------------------------------------------- #

    def create_place(self, place_data):
        """Create place."""
        owner = self.get_user(place_data['owner_id'])
        if not owner:
            raise Exception("Owner not found")
        place = Place(
            title=place_data['title'],
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            owner=owner,
            description=place_data.get('description')
        )
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Retrieve place's data."""
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """Retrieve all places."""
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """Update the place's data."""
        place = self.place_repo.get(place_id)
        if place is None:
            return None

        owner = self.get_user(place_data.get('owner_id', place.owner.uuid))
        if not owner:
            raise Exception("Owner not found")

        place.update_place(
            new_title=place_data.get('title', place.title),
            price=place_data.get('price', place.price),
            latitude=place_data.get('latitude', place.latitude),
            longitude=place_data.get('longitude', place.longitude),
            owner=owner,
            new_description=place_data.get('description', place.description)
        )

        self.place_repo.update(place_id, place.__dict__)
        return place
    
    def add_amenities(self, place_id, amenity_id):
        """Add amenity for the place."""

    # ----------------------------------------------------------- #
    #########################_AMENITY_#############################
    # ----------------------------------------------------------- #

    def create_amenity(self, amenity_data):
        """Create an amenity."""
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Retrieve the amenity's detail."""
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """Retrieve all amenities."""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """Update the amenity."""
        amenity = self.amenity_repo.get(amenity_id)
        if amenity is None:
            return None

        self.amenity_repo.update(amenity_id, amenity_data)
        return self.amenity_repo.get(amenity_id)

    # ----------------------------------------------------------- #
    #########################_REVIEW_##############################
    # ----------------------------------------------------------- #

    def create_review(self, review_data):
        """Create an review."""
        user = self.get_user(review_data['user_id'])
        if not user:
            raise Exception("User not found")

        place = self.get_place(review_data['place_id'])
        if not place:
            raise Exception("Place not found")

        review = Review(
            text=review_data['text'],
            rating=review_data['rating'],
            user_id=review_data['user_id'],
            place_id=review_data['place_id']
        )

        self.review_repo.add(review)
        return review

    def get_all_reviews(self):
        """Retrieve all review's data."""
        return self.review_repo.get_all()

    def get_review(self, review_id):
        """Retrieve review's data."""
        return self.review_repo.get(review_id)

    def update_review(self, review_id, review_data):
        """Update the review."""
        review = self.review_repo.get(review_id)
        if review is None:
            return None

        review.update_review(
            text=review_data.get('text'),
            rating=review_data.get('rating')
        )
        self.review_repo.update(review_id, review.__dict__)
        return review

    def delete_review(self, review_id):
        """Update the review."""
        review = self.review_repo.get(review_id)
        if review is None:
            return None
        self.review_repo.delete(review_id)
        
        return review_id