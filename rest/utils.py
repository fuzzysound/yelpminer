"""
Utility functions for the app.
"""
from ast import literal_eval
import re
from typing import Tuple
from rest.es_query import QueryBuilder


def preprocess_raw_json(data: dict) -> None:
    """
    Preprocess raw Yelp JSON data.
    """
    decode_nested_json(data)
    remove_null_values(data)
    cast_bool_to_str(data)
    remove_nested_quote(data)


def remove_null_values(data: dict) -> None:
    """
    Remove any key whose value indicates null.
    """
    key_to_remove = []
    for k, v in data.items():
        if v is None or v == 'None':
            key_to_remove.append(k)
        elif isinstance(v, dict):
            remove_null_values(v)
    for k in key_to_remove:
        data.pop(k)


def cast_bool_to_str(data: dict) -> None:
    """
    Change boolean value to string, since it is more compatible with Elasticsearch.
    """
    for k, v in data.items():
        if isinstance(v, str) and v in ['True', 'False']:
            data[k] = v.lower()
        elif isinstance(v, bool):
            data[k] = "true" if v else "false"
        elif isinstance(v, dict):
            cast_bool_to_str(v)


def remove_nested_quote(data: dict) -> None:
    """
    Some values are double quoted, e.g. "'free'"
    Change them to right form.
    """
    for k, v in data.items():
        if isinstance(v, str):
            nested = re.findall("'([^']+)'|\"([^\"]+)\"", v)
            if nested:
                data[k] = nested[0][0] if nested[0][0] else nested[0][1]
        elif isinstance(v, dict):
            remove_nested_quote(v)


def decode_nested_json(data: dict) -> None:
    """
    Some values in raw Yelp JSON data are quoted JSON objects, e.g. "{'k1': 'v1', 'k2': 'v2', ... }"
    Remove the quotes and make them Python dictionaries.
    """
    for k in data.keys():
        if isinstance(data[k], str) and k != "text" and data[k] and \
                        data[k][0] == '{' and data[k][-1] == '}':
            data[k] = literal_eval(data[k])
        if isinstance(data[k], dict):
            decode_nested_json(data[k])


def flatten_business_attributes(data: dict) -> None:
    """
    Some values in business attributes are nested JSON objects, e.g.
    {"BusinessParking": {
        "garage": "true",
        "valet": "true",
        "lot": "false",
    }}
    Flatten them for the ease of query simplicity, e.g.
    {"BusinessParking": ["garage", "valet"]}
    """
    if "attributes" not in data.keys():
        return
    for k, v in data["attributes"].items():
        if isinstance(v, dict):
            flattened_value = []
            for subattr, value in v.items():
                if value == "true":
                    flattened_value.append(subattr)
            data["attributes"][k] = flattened_value

def params_to_query_data(params: dict) -> dict:
    """
    Build base query data from the given HTTP GET parameters.
    """
    data = {index: {"query_dsl": QueryBuilder()} for index in ["business", "review", "tip"]}
    data["business"]["query_dsl"].set_pagination_params(params["limit"], params["offset"])
    data["business"]["query_dsl"].set_sort(params["business-sort-by"])

    if params["review-join"] == "true":
        data["review"]["join"] = True
        data["review"]["query_dsl"].set_pagination_params(params["num-reviews"], 0)
        data["review"]["query_dsl"].set_sort(params["review-sort-by"])
    else:
        data["review"]["join"] = False

    if params["tip-join"] == "true":
        data["tip"]["join"] = True
        data["tip"]["query_dsl"].set_pagination_params(params["num-tips"], 0)
        data["tip"]["query_dsl"].set_sort(params["tip-sort-by"])
    else:
        data["tip"]["join"] = False

    for k, v in params.items():
        index, operator, field = dissolve_param_key(k)
        if index in ["business", "review", "tip"]:
            data[index]["query_dsl"].insert_clause(operator, field, v)
    return data


def dissolve_param_key(param_key: str) -> Tuple[str, str, str]:
    """
    Dissolve parameter key to its components, e.g.
    "business__attributes__Parking__in" ->
    index: "business"
    operator: "in",
    field: "attributes.Parking"
    """
    query_components = param_key.split("__")
    index = query_components[0]
    operator = query_components[-1]
    field = '.'.join(query_components[1:-1])
    return index, operator, field

