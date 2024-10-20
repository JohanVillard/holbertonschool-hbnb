from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace("Reviews", description="Review operations")

review_model = api.model(
    "Review",
    {
        "text": fields.String(required=True, description="Text of the review"),
        "rating": fields.String(required=True, description="Rating of the review"),
        "place_id": fields.String(required=True, description="Place of the review"),
        "user_id": fields.String(required=True, description="User writing the review"),
    },
)

facade = HBnBFacade()


@api.route("/")
class ReviewList(Resource):
    @api.expect(review_model, validate=True)
    @api.response(201, "Review successfully created")
    @api.response(400, "Invalid input data")
    def post(self):
        """Register a new review."""
        try:
            review_data = api.payload
            new_review = facade.create_review(review_data)
            user = facade.get_user(new_review.user_id)
            place = facade.get_place(new_review.place_id)
            user.add_review(new_review.uuid)
            place.add_review(new_review.uuid)
            return {
                "id": new_review.uuid,
                "text": new_review.text,
                "rating": new_review.rating,
                "place_id": new_review.place_id,
                "user_id": new_review.user_id,
                "created_at": new_review.created_at.isoformat(),
                "updated_at": new_review.updated_at.isoformat(),
            }, 201
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, "List of reviews retrieved successfully")
    @api.response(404, "Any review found")
    def get(self):
        """Retrieve a list of all reviews."""
        try:
            reviews_list = facade.get_all_reviews()
            if not reviews_list:
                return {"message": "No review found"}, 404
            return [
                {
                    "id": review.uuid,
                    "user_id": review.user_id,
                    "place_id": review.place_id,
                    "rating": review.rating,
                    "text": review.text,
                }
                for review in reviews_list
            ], 200
        except ValueError as e:
            return {"error": str(e)}, 400


@api.route("/<review_id>")
class ReviewResource(Resource):
    @api.response(200, "Display review details by ID.")
    @api.response(404, "Review not found")
    def get(self, review_id):
        """Display review detail by ID."""
        try:
            review = facade.get_review(review_id)
            if not review:
                return {"error": "Review not found"}, 404
            return {
                "id": review.uuid,
                "user_id": review.user_id,
                "place_id": review.place_id,
                "rating": review.rating,
                "text": review.text,
                "created_at": review.created_at.isoformat(),
                "updated_at": review.updated_at.isoformat(),
            }, 200
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, "Review details modified successfully")
    @api.response(404, "Review not found")
    def put(self, review_id):
        """Modify review detail by ID."""
        try:
            review = facade.get_review(review_id)
            if not review:
                return {"error": "Review not found"}, 404

            review_data = api.payload
            facade.update_review(review_id, review_data)
            return {"message": "Review updated successfully"}, 200
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(204, "Review successfully deleted")
    @api.response(404, "Review not found")
    def delete(self, review_id):
        """Delete review by ID."""
        try:
            review = facade.get_review(review_id)
            if not review:
                return {"error": "Review not found"}, 404
            facade.delete_review(review_id)
            user = facade.get_user(review.user_id)
            place = facade.get_place(review.place_id)
            user.delete_review(review_id)
            place.delete_review(review_id)
            return {"message": "Review deleted successfully"}, 204
        except ValueError as e:
            return {"error": str(e)}, 400


@api.route("/place/<place_id>")
class PlaceReview(Resource):
    @api.response(200, "Place's reviews retrieved successfully")
    @api.response(404, "Place not found or no reviews")
    def get(self, place_id):
        """Get place reviews by ID."""
        try:
            place = facade.get_place(place_id)
            if not place:
                return {"error": "Place not found"}, 404
            reviews_list = place.reviews
            if not reviews_list:
                return {"message": "No reviews found for this place"}, 404
            return [
                {
                    "reviews": review,
                }
                for review in reviews_list
            ], 200
        except ValueError as e:
            return {"error": str(e)}, 400


@api.route("/user/<user_id>")
class UserReview(Resource):
    @api.response(200, "User's reviews retrieved successfully")
    @api.response(404, "User not found or no reviews")
    def get(self, user_id):
        """Get user reviews by ID."""
        try:
            print(user_id)
            user = facade.get_user(user_id)
            if not user:
                return {"error": "User not found"}, 404
            reviews_list = user.reviews
            if not reviews_list:
                return {"message": "No reviews found for this user"}, 404
            return [
                {
                    "reviews": review,
                }
                for review in reviews_list
            ], 200
        except ValueError as e:
            return {"error": str(e)}, 400
