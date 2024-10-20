import unittest
from app.models.review import (
    Review,
)
from datetime import datetime
from app.models.place import Place
from app.models.user import User


class TestReview(unittest.TestCase):
    def setUp(self):
        """Initialisation des objets User et Place pour les tests."""
        self.valid_user = User("John", "Doe", "john.doe@example.com")
        self.valid_place = Place(
            "Beautiful House", 150.0, 34.05, -118.25, self.valid_user.uuid
        )
        self.valid_text = "This place is amazing!"
        self.valid_rating = 5
        self.review = Review(
            self.valid_text,
            self.valid_rating,
            self.valid_user.uuid,
            self.valid_place.uuid,
        )

    def test_create_review(self):
        """Test la création d'une revue avec des attributs valides."""
        self.assertEqual(self.review.text, self.valid_text)
        self.assertEqual(self.review.rating, self.valid_rating)
        self.assertIsNotNone(self.review.uuid)  # Vérifie que l'UUID est généré
        self.assertIsInstance(
            self.review.created_at, datetime
        )  # Vérifie que created_at est un datetime

    def test_empty_text(self):
        """Test la création d'une revue avec un texte vide."""
        with self.assertRaises(ValueError):
            Review("", self.valid_rating, self.valid_user.uuid, self.valid_place.uuid)

    def test_invalid_rating_too_low(self):
        """Test la création d'une revue avec une note trop basse."""
        with self.assertRaises(ValueError):
            Review("Great place!", 0, self.valid_user.uuid, self.valid_place.uuid)

    def test_invalid_rating_too_high(self):
        """Test la création d'une revue avec une note trop haute."""
        with self.assertRaises(ValueError):
            Review("Great place!", 6, self.valid_user.uuid, self.valid_place.uuid)

    def test_invalid_rating_type(self):
        """Test la création d'une revue avec un type de note invalide."""
        with self.assertRaises(ValueError):
            Review("Great place!", "five", self.valid_user.uuid, self.valid_place.uuid)

    def test_update_review(self):
        """Test la mise à jour d'une revue."""
        self.review.update_review(text="Updated review", rating=4)
        self.assertEqual(self.review.text, "Updated review")
        self.assertEqual(self.review.rating, 4)

    def test_update_empty_text(self):
        """Test la mise à jour d'une revue avec un texte vide."""
        with self.assertRaises(ValueError):
            self.review.update_review(text="")

    def test_update_invalid_rating(self):
        """Test la mise à jour d'une revue avec une note invalide."""
        with self.assertRaises(ValueError):
            self.review.update_review(rating=10)


if __name__ == "__main__":
    unittest.main()
