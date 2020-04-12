"""
View classes of the app.
"""
from django.views.generic import TemplateView
from elasticsearch import Elasticsearch
from typing import List
from ui.business_attributes import BOOLEAN_ATTRIBUTES, CHOICE_ATTRIBUTES
from ui.operator_map import OPERATOR_MAP
from es_client import client

class YelpminerView(TemplateView):
    """
    View class of Yelpminer.
    """
    template_name = "mainpage.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.select_data = None

    def get_context_data(self, **kwargs):
        """
        Add needed data to context data and hand it to the template.
        """
        context = super().get_context_data(**kwargs)
        if not self.select_data:
            self.select_data = self.get_select_data()
        context["select_data"] = self.select_data
        context["boolean_attributes"] = BOOLEAN_ATTRIBUTES
        context["choice_attributes"] = CHOICE_ATTRIBUTES
        context["operator_map"] = OPERATOR_MAP
        return context

    def get_select_data(self):
        """
        Get data for Select2 selectboxes.
        """
        select_data = {}
        select_data["city"] = self.get_unique_values("business", "city")
        select_data["state"] = self.get_unique_values("business", "state")
        select_data["categories"] = self.get_unique_values("business", "categories")
        return select_data

    @staticmethod
    def get_unique_values(index: str, field: str) -> List[str]:
        """
        Get all unique values of the given index and field.
        """
        query = {
            "size": 0,
            "aggs": {
                "uniq": {
                    "terms": {
                        "field": field
                    }
                }
            }
        }
        sub_result = client.search(index=index, body=query)
        limit = sum([b["doc_count"] for b in sub_result["aggregations"]["uniq"]["buckets"]]) + \
                sub_result["aggregations"]["uniq"]["sum_other_doc_count"]
        query["aggs"]["uniq"]["terms"]["size"] = limit
        result = client.search(index=index, body=query)
        unique_values = []
        for i, b in enumerate(result["aggregations"]["uniq"]["buckets"]):
            unique_values.append({
                "id": i,
                "text": b["key"]
            })
        unique_values.sort(key=lambda x: x["text"])
        return unique_values
