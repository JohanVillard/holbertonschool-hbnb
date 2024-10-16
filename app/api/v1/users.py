from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace("users", description="User operations")

# Define the user model for input validation and documentation
user_model = api.model(
    "User",
    {
        "first_name": fields.String(
            required=True, description="First name of the user"
        ),
        "last_name": fields.String(required=True, description="Last name of the user"),
        "email": fields.String(required=True, description="Email of the user"),
    },
)

facade = HBnBFacade()


@api.route("/")
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, "User successfully created")
    @api.response(400, "Email already registered")
    @api.response(400, "Invalid input data")
    def post(self):
        """Register a new user."""
        try:
            user_data = api.payload

            # Simulate email uniqueness check (to be replaced by real validation with persistence)
            existing_user = facade.get_user_by_email(user_data["email"])
            if existing_user:
                return {"error": "Email already registered"}, 400

            new_user = facade.create_user(user_data)
            return {
                "id": new_user.uuid,
                "first_name": new_user.first_name,
                "last_name": new_user.last_name,
                "email": new_user.email,
                "created_at": new_user.created_at.isoformat(),
                "updated_at": new_user.updated_at.isoformat(),
        }, 201
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, "List of users retrieved successfully")
    @api.response(404, "User not found")
    def get(self):
        """Retrieve a list of all users."""
        try:
            users_list = facade.get_all_users()

            if not users_list:
                return {"message": "No user found"}, 404

            # Get the name of each user
            return [
                {
                    "id": user.uuid,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                }
                for user in users_list
            ], 200
        except ValueError as e:
            return {"error": str(e)}, 400



@api.route("/<user_id>")
class UserResource(Resource):
    @api.response(200, "User details retrieved successfully")
    @api.response(404, "User not found")
    def get(self, user_id):
        """Get user details by ID."""
        try:
            user = facade.get_user(user_id)
            if not user:
                return {"error": "User not found"}, 404
            return {
                "id": user.uuid,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "created_at": user.created_at.isoformat(),
                "updated_at": user.updated_at.isoformat(),
            }, 200
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.expect(user_model, validate=True)
    @api.response(200, "User details updated successfully")
    @api.response(404, "User not found")
    def put(self, user_id):
        """Modify user details."""
        user = facade.get_user(user_id)
        if not user:
            return {"error": "User not found"}, 404
        try:
            user_data = api.payload
            updated_user = facade.update_user(user_id, user_data)

            return {
                "id": updated_user.uuid,
                "first_name": updated_user.first_name,
                "last_name": updated_user.last_name,
                "email": updated_user.email,
                "created_at": updated_user.created_at.isoformat(),
                "updated_at": updated_user.updated_at.isoformat(),
            }, 200
        except ValueError as e:
            return {"error": str(e)}, 400
