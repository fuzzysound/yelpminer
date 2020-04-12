"""
Bulk Yelp JSON files to Elasticsearch.
"""
from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch, helpers
import json
from rest.es_mappings import BUSINESS_MAPPINGS, REVIEW_MAPPINGS, TIP_MAPPINGS
from rest.es_filepaths import BUSINESS_FP, REVIEW_FP, TIP_FP
from rest import utils
from es_client import client


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = client

    def handle(self, *args, **options):
        """
        Main method of the command.
        """
        self.create_indices()
        self.bulk()

    def create_indices(self) -> None:
        """
        Create needed indices in Elasticsearch.
        """
        self.client.indices.create(
            index="business",
            body=BUSINESS_MAPPINGS
        )
        self.client.indices.create(
            index="review",
            body=REVIEW_MAPPINGS
        )
        self.client.indices.create(
            index="tip",
            body=TIP_MAPPINGS
        )

    def bulk(self) -> None:
        """
        Bulk each JSON data into Elasticsearch.
        """
        helpers.bulk(self.client, self.gen_business_data(BUSINESS_FP))
        helpers.bulk(self.client, self.gen_review_data(REVIEW_FP))
        helpers.bulk(self.client, self.gen_tip_data(TIP_FP))

    @staticmethod
    def gen_business_data(fp: str) -> None:
        """
        Preprocess and generate business data.
        """
        with open(fp, encoding='utf-8') as f:
            for line in f:
                data = json.loads(line)
                if "categories" in data.keys() and data["categories"]:
                    data["categories"] = [s.strip() for s in data["categories"].split(',')]
                utils.preprocess_raw_json(data)
                utils.flatten_business_attributes(data)
                doc = {
                    "_index": "business",
                    "_source": data
                }
                yield doc

    @staticmethod
    def gen_review_data(fp: str) -> None:
        """
        Preprocess and generate review data.
        """
        with open(fp, encoding='utf-8') as f:
            for line in f:
                data = json.loads(line)
                utils.preprocess_raw_json(data)
                doc = {
                    "_index": "review",
                    "_source": data
                }
                yield doc

    @staticmethod
    def gen_tip_data(fp: str) -> None:
        """
        Preprocess and generate tip data.
        """
        with open(fp, encoding='utf-8') as f:
            for line in f:
                data = json.loads(line)
                utils.preprocess_raw_json(data)
                doc = {
                    "_index": "tip",
                    "_source": data
                }
                yield doc
