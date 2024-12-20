from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace("Places", description="Place operations")

place_model = api.model(
    "Place",
    {
        "title": fields.String(required=True, description="Title of the place"),
        "price": fields.Float(required=True, description="Price per night"),
        "latitude": fields.Float(required=True, description="Latitude of the place"),
        "longitude": fields.Float(required=True, description="Longitude of the place"),
        "owner_id": fields.String(required=True, description="ID of the owner"),
        "description": fields.String(description="Description of the place"),
    },
)

facade = HBnBFacade()


@api.route("/")
class PlaceList(Resource):
    @api.expect(place_model, validate=True)
    @api.response(201, "Place successfully created")
    @api.response(400, "Invalid input data")
    @api.response(404, "Owner not found")
    def post(self):
        """Create a new place."""
        try:
            place_data = api.payload
            new_place = facade.create_place(place_data)
            new_place.owner.add_place(new_place.uuid)
            return {
                "id": new_place.uuid,
                "title": new_place.title,
                "price": new_place.price,
                "latitude": new_place.latitude,
                "longitude": new_place.longitude,
                "owner": {
                    "id": new_place.owner.uuid,
                    "first_name": new_place.owner.first_name,
                    "last_name": new_place.owner.last_name,
                },
                "description": new_place.description,
                "created_at": new_place.created_at.isoformat(),
                "updated_at": new_place.updated_at.isoformat(),
            }, 201
        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception:
            return {"error": "Owner not found"}, 404

    @api.response(200, "List of places retrieved successfully")
    def get(self):
        """Retrieve a list of all places."""
        places = facade.get_all_places()
        return [
            {
                "id": place.uuid,
                "title": place.title,
                "price": place.price,
                "latitude": place.latitude,
                "longitude": place.longitude,
                "owner": {
                    "id": place.owner.uuid,
                    "first_name": place.owner.first_name,
                    "last_name": place.owner.last_name,
                },
                "description": place.description,
                "reviews": len(place.reviews),
            }
            for place in places
        ], 200


@api.route("/<place_id>")
class PlaceResource(Resource):
    @api.response(200, "Place details retrieved successfully")
    @api.response(404, "Place not found")
    def get(self, place_id):
        """Get place details by ID."""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        return {
            "id": place.uuid,
            "title": place.title,
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": {
                "id": place.owner.uuid,
                "first_name": place.owner.first_name,
                "last_name": place.owner.last_name,
            },
            "description": place.description,
            "amenities": [
                {"id": amenity.uuid, "name": amenity.name}
                for amenity in place.amenities
            ],
            # "reviews": [{"id": review.id, "user": review.user, "description": review.text} for review in place.reviews],
            "reviews": place.reviews,
            "created_at": place.created_at.isoformat(),
            "updated_at": place.updated_at.isoformat(),
        }, 200

    @api.expect(place_model)
    @api.response(200, "Place details updated successfully")
    @api.response(404, "Place not found")
    @api.response(400, "Invalid input data")
    def put(self, place_id):
        """Modify place details."""
        try:
            place_data = api.payload
            updated_place = facade.update_place(place_id, place_data)
            if not updated_place:
                return {"error": "Place not found"}, 404
            return {"message": "Place updated successfully"}, 200
        except ValueError as e:
            return {"error": str(e)}, 400


@api.route("/<place_id>/add_amenity/<amenity_id>")
class PlaceAmenity(Resource):
    @api.response(200, "Place and amenity are now associated.")
    @api.response(404, "Place not found")
    @api.response(404, "Amenity not found")
    def post(self, place_id, amenity_id):
        """Associate an amenity to a place."""
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, "Place not found")

        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, "Amenity not found")

        facade.associate_place_to_amenity(place_id, amenity_id)
        return {"message": "Place and amenity are now associated."}, 200


@api.route("/<place_id>/reviews")
class PlaceReview(Resource):
    @api.response(200, "Place's reviews retrieved successfully")
    @api.response(404, "Place not found or no reviews")
    def get(self, place_id):
        """Get places's reviews by ID."""
        try:
            place = facade.get_place(place_id)
            if not place:
                return {"error": "Place not found"}, 404

            reviews_list = place.reviews
            if not reviews_list:
                return {"message": "No reviews found for this place"}, 404
            return [
                {
                    "id": review_id,
                    "text": facade.get_review(review_id).text,
                    "rating": facade.get_review(review_id).rating,
                }
                for review_id in reviews_list
            ], 200
        except ValueError as e:
            return {"error": str(e)}, 400
