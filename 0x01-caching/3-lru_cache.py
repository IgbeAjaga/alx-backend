#!/usr/bin/env python3
""" 3-lru_cache """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        super().__init__()
        self.access_tracker = []

    def put(self, key, item):
        """ Put method """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                removed = self.access_tracker.pop(0)
                del self.cache_data[removed]
                print(f"DISCARD: {removed}")
            self.cache_data[key] = item
            self.access_tracker.append(key)

    def get(self, key):
        """ Get method """
        if key in self.cache_data:
            self.access_tracker.remove(key)
            self.access_tracker.append(key)
            return self.cache_data[key]
        return None
