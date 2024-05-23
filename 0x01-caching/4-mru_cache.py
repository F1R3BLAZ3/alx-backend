#!/usr/bin/env python3
"""
mru_cache.py
This module provides an MRUCache class that inherits from BaseCaching and
implements a Most Recently Used (MRU) caching system.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that inherits from BaseCaching.
    It discards the most recently used items when the cache exceeds its limit.
    """

    def __init__(self):
        """
        Initialize the MRUCache instance.
        """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.mru_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.mru_order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            self.cache_data[key] = item
            self.mru_order.append(key)

    def get(self, key):
        """
        Get an item by key from the cache.

        Args:
            key (str): The key to look up in the cache.

        Returns:
            any: The item stored under the key/None if the key doesn't exist.
        """
        if key is not None and key in self.cache_data:
            self.mru_order.remove(key)
            self.mru_order.append(key)
            return self.cache_data[key]
        return None
