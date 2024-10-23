class PlaceAmenityAssociation:
    def __init__(self, place_id, amenity_id):
        self.uuid = "association"
        self.association = (place_id, amenity_id)
