#!/usr/bin/env python3
""" 1-fifo_cache """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """

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
        return self.cache_data.get(key) if key in self.cache_data else None
