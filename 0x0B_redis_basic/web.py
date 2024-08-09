#!/usr/bin/env python3
""" Redis exercise """

import requests
import redis
from typing import Callable
from functools import wraps

r = redis.Redis()


def get_page_count(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs
    """
    @wraps(method)
    def count(url):
        """method to count"""
        r.incr(f"count:{url}")
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode("utf-8")
        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html
    return count


@get_page_count
def get_page(url: str) -> str:
    """
    Get a page
    """
    content = requests.get(url)
    return content.text
