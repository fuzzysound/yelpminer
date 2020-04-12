"""
Extra template filters for the app.
"""
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="rowstart")
def row_start(forloop: dict) -> bool:
    """
    Check if start of Bootstrap row.
    """
    return int(forloop["counter0"]) % 3 == 0

@register.filter(name="rowend")
def row_end(forloop: dict) -> bool:
    """
    Check if end of Bootstrap row.
    """
    return int(forloop["counter0"]) % 3 == 2 or forloop["last"]

@register.filter(name="genattrid")
@stringfilter
def generate_attr_id(attr_name: str) -> str:
    """
    Generate element id of the business attribute.
    """
    return "business__attributes__" + attr_name

@register.filter(name="gencheckboxid")
@stringfilter
def generate_checkbox_id(attr_name: str) -> str:
    """
    Generate element id of the business attribute checkbox.
    """
    return "business__attributes__" + attr_name + "-checkbox"

@register.filter(name="gensubattrid")
@stringfilter
def generate_subattr_id(subattr_name: str, attr_name: str) -> str:
    """
    Generate element id of the sub-attribute of business attribute.
    """
    return "business__attributes__" + attr_name + "__" + subattr_name
