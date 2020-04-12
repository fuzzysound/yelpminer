"""
Package to build Elasticsearch query.
"""
from collections import defaultdict

class QueryBuilder:
    """
    Elasticsearch query builder class.
    """
    def __init__(self):
        self.query = {
            "query": {
                "bool": defaultdict(list),
            }
        }

    def insert_clause(self, operator: str, field: str, value: str) -> None:
        """
        Insert clause to query according to the given operator.
        We can have 4 types of operators.
        - contains: field is a text and must match at least one of the keyword (given being joined with comma).
        - in: field is a keyword or array of keywords and must have one of the keyword (given being joined with comma).
        - eq: field must exactly match the given value.
        - range: field is a number or date, and must be inside the given range (given being joined with comma).
        """
        if operator == "contains":
            bool_q = {"bool": {"should": []}}
            arr = [s.strip() for s in value.split(',')]
            for key in arr:
                q = {"match_phrase": {field: key}}
                bool_q["bool"]["should"].append(q)
            self.query["query"]["bool"]["filter"].append(bool_q)
        elif operator == "in":
            arr = [s.strip() for s in value.split(',')]
            q = {"terms": {field: arr}}
            self.query["query"]["bool"]["filter"].append(q)
        elif operator == "eq":
            q = {"term": {field: value}}
            self.query["query"]["bool"]["filter"].append(q)
        elif operator == "range":
            gte, lte = value.split(',')
            q = {"range": {field: {"gte": gte, "lte": lte}}}
            self.query["query"]["bool"]["filter"].append(q)

    def update_clause(self, operator: str, field: str, value: str) -> None:
        """
        Update clause in query of the given operator and field by the given value.
        'contains' operator is not supported.
        """
        for q in self.query["query"]["bool"]["filter"]:
            if operator == "in":
                arr = [s.strip() for s in value.split(',')]
                if "terms" in q.keys() and field in q["terms"].keys():
                    q["terms"][field] = arr
                    return
            elif operator == "eq":
                if "term" in q.keys() and field in q["term"].keys():
                    q["term"][field] = value
                    return
            elif operator == "range":
                gte, lte = value.split(',')
                if "range" in q.keys() and field in q["range"].keys():
                    q["range"][field]["gte"] = gte
                    q["range"][field]["lte"] = lte
                    return

    def set_pagination_params(self, limit: str, offset: str) -> None:
        """
        Set limit and offset value for pagination.
        """
        self.query["size"] = limit
        self.query["from"] = offset

    def get_page(self) -> int:
        """
        Get page number. Page number starts at 1.
        """
        return int(self.query["from"]) // int(self.query["size"]) + 1

    def get_limit(self) -> int:
        """
        Get limit value.
        """
        return int(self.query["size"])

    def set_sort(self, field: str, desc: bool=True) -> None:
        """
        Set sort field. Descending order is default.
        """
        self.query["sort"] = {}
        self.query["sort"][field] = "desc" if desc else "asc"

    def get_query(self) -> dict:
        """
        Get the query to use at Elasticsearch POST request.
        """
        return self.query
