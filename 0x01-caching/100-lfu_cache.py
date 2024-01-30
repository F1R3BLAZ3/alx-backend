#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize LFUCache
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # LFU: Discard the least frequency used item
                discarded_key = min(
                    self.frequency, key=lambda k: self.frequency[k])
                if list(self.frequency.values()).count(
                        self.frequency[discarded_key]) > 1:
                    # If there are ties, use LRU algorithm to break the tie
                    self.lru_discard()
                else:
                    # Discard the least frequency used item
                    del self.cache_data[discarded_key]
                    del self.frequency[discarded_key]
                    print("DISCARD:", discarded_key)

            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Update frequency to indicate recent usage
            self.frequency[key] += 1
            return self.cache_data[key]
        return None

    def lru_discard(self):
        """ LRU Discard helper function
        """
        discarded_key = min(self.cache_data, key=lambda k: self.cache_data[k])
        del self.cache_data[discarded_key]
        del self.frequency[discarded_key]
        print("DISCARD:", discarded_key)
