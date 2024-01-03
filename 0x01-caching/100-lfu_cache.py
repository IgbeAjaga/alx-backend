#!/usr/bin/env python3
""" 100-lfu_cache """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class """

    def __init__(self):
        super().__init__()
        self.freq_tracker = {}
        self.freq = {}

    def put(self, key, item):
        """ Put method """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.freq.values())
                items_min_freq = [k for k, v in self.freq.items() if v == min_freq]
                if len(items_min_freq) > 1:
                    lru = min(self.freq_tracker[items_min_freq[0]], self.freq_tracker[items_min_freq[1]])
                    removed = [k for k, v in self.freq_tracker.items() if v == lru][0]
                else:
                    removed = items_min_freq[0]
                del self.freq[removed]
                del self.freq_tracker[removed]
                del self.cache_data[removed]
                print(f"DISCARD: {removed}")
            self.cache_data[key] = item
            if key in self.freq:
                self.freq[key] += 1
            else:
                self.freq[key] = 1
            self.freq_tracker[key] = self.timestamp()

    def get(self, key):
        """ Get method """
        if key in self.cache_data:
            self.freq[key] += 1
            self.freq_tracker[key] = self.timestamp()
            return self.cache_data[key]
        return None

    def timestamp(self):
        """ Timestamp """
        return len(self.freq_tracker)
