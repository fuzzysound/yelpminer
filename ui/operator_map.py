"""
Data containing fields and corresponding operators.
"""
from collections import OrderedDict

OPERATOR_MAP = OrderedDict({
    "business": {
        "name": "contains",
        "city": "eq",
        "state": "eq",
        "categories": "in",
        "stars": "range",
        "is_open": "eq",
        "attributes": {
            "BusinessAcceptsCreditCards": "eq",
            "BikeParking": "eq",
            "GoodForKids": "eq",
            "BusinessParking": "in",
            "ByAppointmentOnly": "eq",
            "DogsAllowed": "eq",
            "WiFi": "in",
            "RestaurantsAttire": "in",
            "RestaurantsTakeOut": "eq",
            "NoiseLevel": "in",
            "RestaurantsReservations": "eq",
            "RestaurantsGoodForGroups": "eq",
            "HasTV": "eq",
            "Alcohol": "in",
            "RestaurantsDelivery": "eq",
            "OutdoorSeating": "eq",
            "Caters": "eq",
            "WheelchairAccessible": "eq",
            "AcceptsInsurance": "eq",
            "RestaurantsTableService": "eq",
            "Ambience": "in",
            "GoodForMeal": "in",
            "HappyHour": "eq",
            "BusinessAcceptsBitcoin": "eq",
            "BYOB": "eq",
            "Corkage": "eq",
            "GoodForDancing": "eq",
            "CoatCheck": "eq",
            "Music": "in",
            "Smoking": "in",
            "DietaryRestrictions": "in",
            "DriveThru": "eq",
            "HairSpecializesIn": "in",
            "BYOBCorkage": "in",
            "AgesAllowed": "in",
            "RestaurantsCounterServices": "eq",
            "Open24Hours": "eq"
        }
    },
    "review": {
        "stars": "range",
        "text": "contains",
        "date": "range"
    },
    "tip": {
        "text": "contains",
        "date": "range"
    }
})