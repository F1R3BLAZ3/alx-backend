#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize LRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # LRU: Discard the least recently used item
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Update order to indicate recent usage
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
