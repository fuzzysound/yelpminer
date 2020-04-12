"""
Package to build JSON response.
"""
from django.urls import reverse
from django.http import HttpRequest
from urllib.parse import urlencode
from collections import OrderedDict
from rest import utils
from es_client import client


class JSONResponseBuilder:
    """
    JSON response builder class.
    """
    def __init__(self):
        self.client = client
        self.total_count = 0
        self.size = 0
        self.hits = []

    def build(self, request: HttpRequest) -> OrderedDict:
        """
        Get the query result from Elasticsearch with given Django HttpRequest object and build JSON data
        for response.
        """
        query_data = utils.params_to_query_data(request.query_params)
        self.get_business_data(query_data)
        if query_data["review"]["join"]:
            self.attach_reviews_or_tips(query_data, "review")
        if query_data["tip"]["join"]:
            self.attach_reviews_or_tips(query_data, "tip")
        json_response = OrderedDict({
            "totalCount": self.total_count,
            "page": query_data["business"]["query_dsl"].get_page(),
            "perPage": query_data["business"]["query_dsl"].get_limit(),
            "hits": self.business_data
        })

        # Attach URL of next page if any page is left.
        if json_response["totalCount"] > json_response["page"] * json_response["perPage"]:
            uri = request.build_absolute_uri(reverse("query_es"))
            new_params = request.query_params.dict()
            new_params["offset"] = json_response["page"] * json_response["perPage"]
            full_url = uri + '?' + urlencode(new_params)
            json_response["next"] = full_url
            json_response.move_to_end("hits")
        return json_response

    def get_business_data(self, query_data: dict) -> None:
        """
        Get queried business data from Elasticsearch.
        """
        result = self.client.search(index="business",
                                    body=query_data["business"]["query_dsl"].get_query())
        self.total_count = int(result["hits"]["total"]["value"])
        self.business_data = [d["_source"] for d in result["hits"]["hits"]]

    def attach_reviews_or_tips(self, query_data: dict, index: str) -> None:
        """
        Attach review or tip data to each business data.
        """
        query_data[index]["query_dsl"].insert_clause("eq", "business_id", "")
        for business in self.business_data:
            business_id = business["business_id"]
            query_data[index]["query_dsl"].update_clause("eq", "business_id", business_id)
            result = self.client.search(index=index,
                                        body=query_data[index]["query_dsl"].get_query())
            review_or_tip_data = [d["_source"] for d in result["hits"]["hits"]]
            business[index + 's'] = review_or_tip_data
