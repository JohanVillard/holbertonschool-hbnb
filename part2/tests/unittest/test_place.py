import unittest
from datetime import datetime
from app.models.place import (
    Place,
)


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Initialisation d'un objet Place valide pour les tests."""
        self.valid_title = "Beautiful House"
        self.valid_price = 150.0
        self.valid_latitude = 34.05
        self.valid_longitude = -118.25
        self.valid_owner = "user_uuid"  # Remplacez par un UUID valide si nécessaire
        self.place = Place(
            self.valid_title,
            self.valid_price,
            self.valid_latitude,
            self.valid_longitude,
            self.valid_owner,
        )

    def test_create_place(self):
        """Test la création d'un lieu avec des attributs valides."""
        self.assertEqual(self.place.title, self.valid_title)
        self.assertEqual(self.place.price, self.valid_price)
        self.assertEqual(self.place.latitude, self.valid_latitude)
        self.assertEqual(self.place.longitude, self.valid_longitude)
        self.assertIsNotNone(self.place.uuid)  # Vérifie que l'UUID est généré
        self.assertIsInstance(
            self.place.created_at, datetime
        )  # Vérifie que created_at est un datetime

    def test_empty_title(self):
        """Test la création d'un lieu avec un titre vide."""
        with self.assertRaises(ValueError):
            Place(
                "",
                self.valid_price,
                self.valid_latitude,
                self.valid_longitude,
                self.valid_owner,
            )

    def test_negative_price(self):
        """Test la création d'un lieu avec un prix négatif."""
        with self.assertRaises(ValueError):
            Place(
                "House",
                -100.0,
                self.valid_latitude,
                self.valid_longitude,
                self.valid_owner,
            )

    def test_zero_price(self):
        """Test la création d'un lieu avec un prix zéro."""
        with self.assertRaises(ValueError):
            Place(
                "House",
                0.0,
                self.valid_latitude,
                self.valid_longitude,
                self.valid_owner,
            )

    def test_invalid_latitude_too_low(self):
        """Test la création d'un lieu avec une latitude trop basse."""
        with self.assertRaises(ValueError):
            Place(
                "House",
                self.valid_price,
                -100.0,
                self.valid_longitude,
                self.valid_owner,
            )

    def test_invalid_latitude_too_high(self):
        """Test la création d'un lieu avec une latitude trop haute."""
        with self.assertRaises(ValueError):
            Place(
                "House", self.valid_price, 100.0, self.valid_longitude, self.valid_owner
            )

    def test_invalid_longitude_too_low(self):
        """Test la création d'un lieu avec une longitude trop basse."""
        with self.assertRaises(ValueError):
            Place(
                "House", self.valid_price, self.valid_latitude, -200.0, self.valid_owner
            )

    def test_invalid_longitude_too_high(self):
        """Test la création d'un lieu avec une longitude trop haute."""
        with self.assertRaises(ValueError):
            Place(
                "House", self.valid_price, self.valid_latitude, 200.0, self.valid_owner
            )


if __name__ == "__main__":
    unittest.main()
