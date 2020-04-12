"""
Elasticsearch mapping of each index.
"""
BUSINESS_MAPPINGS = {
    "mappings": {
        "properties": {
            "business_id": {"type": "keyword"},
            "name": {"type": "text"},
            "address": {"type": "keyword", "index": False},
            "city": {"type": "keyword"},
            "state": {"type": "keyword"},
            "postal_code": {"type": "keyword", "index": False},
            "latitude": {"type": "double"},
            "longitude": {"type": "double"},
            "stars": {"type": "half_float"},
            "review_count": {"type": "integer"},
            "is_open": {"type": "byte"},
            "attributes":{
                "properties": {
                    "BusinessAcceptsCreditCards": {"type": "boolean"},
                    "BikeParking": {"type": "boolean"},
                    "GoodForKids": {"type": "boolean"},
                    "BusinessParking": {"type": "keyword"},
                    "ByAppointmentOnly": {"type": "boolean"},
                    "RestaurantPriceRange2": {"type": "keyword"},
                    "DogsAllowed": {"type": "boolean"},
                    "WiFi": {"type": "keyword"},
                    "RestaurantsAttire": {"type": "keyword"},
                    "RestaurantsTakeOut": {"type": "boolean"},
                    "NoiseLevel": {"type": "keyword"},
                    "RestaurantsReservations": {"type": "boolean"},
                    "RestaurantsGoodForGroups": {"type": "boolean"},
                    "HasTV": {"type": "boolean"},
                    "Alcohol": {"type": "keyword"},
                    "RestaurantsDelivery": {"type": "boolean"},
                    "OutdoorSeating": {"type": "boolean"},
                    "Caters": {"type": "boolean"},
                    "WheelchairAccessible": {"type": "boolean"},
                    "AcceptsInsurance": {"type": "boolean"},
                    "RestaurantsTableService": {"type": "boolean"},
                    "Ambience": {"type": "keyword"},
                    "GoodForMeal": {"type": "keyword"},
                    "HappyHour": {"type": "boolean"},
                    "BusinessAcceptsBitcoin": {"type": "boolean"},
                    "BYOB": {"type": "boolean"},
                    "Corkage": {"type": "boolean"},
                    "GoodForDancing": {"type": "boolean"},
                    "CoatCheck": {"type": "boolean"},
                    "BestNights": {"type": "keyword"},
                    "Music": {"type": "keyword"},
                    "Smoking": {"type": "keyword"},
                    "DietaryRestrictions": {"type": "keyword"},
                    "DriveThru": {"type": "boolean"},
                    "HairSpecializesIn": {"type": "keyword"},
                    "BYOBCorkage": {"type": "keyword"},
                    "AgesAllowed": {"type": "keyword"},
                    "RestaurantsCounterServices": {"type": "boolean"},
                    "Open24Hours": {"type": "boolean"}
                }
            },
            "categories": {"type": "keyword"},
            "hours": {
                "properties": {
                    "Monday": {"type": "keyword", "index": False},
                    "Tuesday": {"type": "keyword", "index": False},
                    "Wednesday": {"type": "keyword", "index": False},
                    "Thursday": {"type": "keyword", "index": False},
                    "Friday": {"type": "keyword", "index": False},
                    "Saturday": {"type": "keyword", "index": False},
                    "Sunday": {"type": "keyword", "index": False},
                }
            }
        }
    }
}


USER_MAPPINGS = {
    "mappings": {
        "properties": {
            "user_id": {"type": "keyword"},
            "name": {"type": "keyword"},
            "review_count": {"type": "integer"},
            "elite": {"type": "boolean"}
        }
    }
}


REVIEW_MAPPINGS = {
    "mappings": {
        "properties": {
            "review_id": {"type": "keyword"},
            "user_id": {"type": "keyword"},
            "business_id": {"type": "keyword"},
            "stars": {"type": "half_float"},
            "useful": {"type": "integer"},
            "funny": {"type": "integer"},
            "cool": {"type": "integer"},
            "text": {"type": "text", "analyzer": "english"},
            "date": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"}
        }
    }
}


TIP_MAPPINGS = {
    "mappings": {
        "properties": {
            "user_id": {"type": "keyword"},
            "business_id": {"type": "keyword"},
            "text": {"type": "text", "analyzer": "english"},
            "date": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"},
            "compliment_count": {"type": "integer"}
        }
    }
}
