#!/usr/bin/env python3
""" 2-lifo_cache """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Put method """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                removed = list(self.cache_data.keys())[-1]
                del self.cache_data[removed]
                print(f"DISCARD: {removed}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get method """
        return self.cache_data.get(key) if key in self.cache_data else None
