#!/usr/bin/env python3
""" 0-basic_cache """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class """

    def put(self, key, item):
        """ Put method """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get method """
        return self.cache_data.get(key) if key in self.cache_data else None
