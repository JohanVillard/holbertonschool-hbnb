from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade

api = Namespace("auth", description="Authentification operations")
facade = HBnBFacade()

# Model for input validation
login_model = api.model(
    "Login",
    {
        "email": fields.String(required=True, description="User email"),
        "password": fields.String(required=True, description="User password"),
    },
)


@api.route("/login")
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authentificate user and return JWT token."""
        credentials = api.payload  # Get the email and password from the request payload

        # Step 1: Retrieve the user based on the provided email
        user = facade.get_user_by_email(credentials["email"])

        # Step 2 : Check if the user exists and the password is correct
        if not user or not user.verify_password(credentials["password"]):
            return {"error": "Invalid credentials"}, 401

        # Step 3: Create a JWT token with the user's id and is_admin flag
        access_token = create_access_token(
            identity=str(user.uuid),  # `sub` va automatiquement recevoir l'ID de l'utilisateur
            additional_claims={
                "is_admin": user.is_admin  # Ajouter `is_admin` comme revendication personnalisée
            }
        ) 

        # Step 4: Return the JWT token to the client
        return {"access_token": access_token}, 200


@api.route("/protected")
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        """A protected endpoint that requires a valid JWT token."""
        current_user = get_jwt_identity()  # Retrieve the user's identity from the token
        return {"message": f"Hello, user {current_user["id"]}"}, 200