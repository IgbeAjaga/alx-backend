#!/usr/bin/env python3
""" 4-mru_cache """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Put method """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                removed = list(self.cache_data.keys())[0]
                del self.cache_data[removed]
                print(f"DISCARD: {removed}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get method """
        if key in self.cache_data:
            del self.cache_data[key]
            self.cache_data[key] = key
            return self.cache_data[key]
        return None
