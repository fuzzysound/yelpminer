"""
Data containing business attributes and their labels.
"""
from collections import OrderedDict

BOOLEAN_ATTRIBUTES = OrderedDict({
    "BusinessAcceptsCreditCards": "Accepts Credit Cards",
    "BikeParking": "Bike Parking",
    "GoodForKids": "Good for Kids",
    "ByAppointmentOnly": "Appointment Only",
    "DogsAllowed": "Dogs Allowed",
    "RestaurantsTakeOut": "Offers Takeout",
    "RestaurantsReservations": "Offers Reservations",
    "RestaurantsGoodForGroups": "Good for Groups",
    "HasTV": "Has TV",
    "RestaurantsDelivery": "Offers Delivery",
    "OutdoorSeating": "Outdoor Seating",
    "Caters": "Caters",
    "WheelchairAccessible": "Wheelchair Accessible",
    "AcceptsInsurance": "Accepts Insurance",
    "RestaurantsTableService": "Offers Table Service",
    "HappyHour": "Good for Happy Hour",
    "BusinessAcceptsBitcoin": "Accepts Bitcoin",
    "BYOB": "BYOB",
    "Corkage": "Corkage Fee",
    "GoodForDancing": "Good for Dancing",
    "CoatCheck": "Offers Coat Check",
    "DriveThru": "Offers Drive Thru",
    "RestaurantsCounterServices": "Offers Counter Services",
    "Open24Hours": "Open 24 Hours"
})

CHOICE_ATTRIBUTES = OrderedDict({
    "BusinessParking": {
        "text": "Parking",
        "choice": {
            "garage": "Garage",
            "street": "Street",
            "validated": "Validated",
            "lot": "Lot",
            "valet": "Valet"
        }
    },
    "WiFi": {
        "text": "WiFi",
        "choice": {
            "free": "Free",
            "paid": "Paid",
            "no": "No WiFi"
        }
    },
    "RestaurantsAttire": {
        "text": "Attire (Restaurants)",
        "choice": {
            "casual": "Casual",
            "dressy": "Dressy",
            "formal": "Formal"
        }
    },
    "NoiseLevel": {
        "text": "Noise Level",
        "choice": {
            "quiet": "Quiet",
            "average": "Average",
            "loud": "Loud",
            "very_loud": "Very Loud",
        }
    },
    "Alcohol": {
        "text": "Alcohol",
        "choice": {
            "beer_and_wine": "Beer & Wine",
            "full_bar": "Full Bar",
            "none": "No Alcohol"
        }
    },
    "Ambience": {
        "text": "Ambience",
        "choice": {
            "touristy": "Touristy",
            "hipster": "Hipster",
            "romantic": "Romantic",
            "divey": "Divey",
            "intimate": "Intimate",
            "trendy": "Trendy",
            "upscale": "Upscale",
            "classy": "Classy",
            "casual": "Casual"
        }
    },
    "GoodForMeal": {
        "text": "Good for Meal at",
        "choice": {
            "dessert": "Dessert",
            "latenight": "Late Night",
            "lunch": "Lunch",
            "dinner": "Dinner",
            "breakfast": "Breakfast",
            "brunch": "Brunch"
        }
    },
    "Music": {
        "text": "Music",
        "choice": {
            "dj": "DJ",
            "background_music": "Background Music",
            "jukebox": "Jukebox",
            "live": "Live",
            "video": "Video",
            "karaoke": "Karaoke",
            "no_music": "No Music"
        }
    },
    "Smoking": {
        "text": "Smoking",
        "choice": {
            "yes": "Yes",
            "outdoor": "Outdoor",
            "no": "No"
        }
    },
    "DietaryRestrictions": {
        "text": "Dietary Restrictions",
        "choice": {
            "dairy-free": "Dairy-free",
            "gluten-free": "Gluten-free",
            "soy-free": "Soy-free",
            "vegan": "Vegan",
            "kosher": "Kosher",
            "halal": "Halal",
            "vegetarian": "Vegetarian"
        }
    },
    "HairSpecializesIn": {
        "text": "Hair Specializes in",
        "choice": {
            "perms": "Perms",
            "straightperms": "Straightperms",
            "coloring": "Coloring",
            "extensions": "Extensions",
            "curly": "Curly",
            "kids": "Kids",
            "africanamerican": "African American",
            "asian": "Asian"
        }
    },
    "BYOBCorkage": {
        "text": "BYOB and Corkage Fee",
        "choice": {
            "yes_corkage": "Yes and Corkage Fee",
            "yes_free": "Yes and Free",
            "no": "No"
        }
    },
    "AgesAllowed": {
        "text": "Ages Allowed",
        "choice": {
            "allages": "All Ages",
            "18plus": "18+",
            "19plus": "19+",
            "21plus": "21+",
        }
    }
})