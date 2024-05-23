#!/usr/bin/env python3
"""
lfu_cache.py
This module provides an LFUCache class that inherits from BaseCaching and
implements a Least Frequently Used (LFU) caching system.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache is a caching system that inherits from BaseCaching.
    It discards the least frequently used items first. In case of a tie,
    the least recently used item is discarded.
    """

    def __init__(self):
        """
        Initialize the LFUCache instance.
        """
        super().__init__()
        self.frequency = {}
        self.recency = {}
        self.time = 0

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.recency[key] = self.time
            self.time += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the LFU item
                min_freq = min(self.frequency.values())
                lfu_keys = [
                    k for k,
                    v in self.frequency.items()
                    if v == min_freq]

                if len(lfu_keys) > 1:
                    # If there's a tie, use LRU to decide which one to discard
                    lru_key = min(lfu_keys, key=lambda k: self.recency[k])
                else:
                    lru_key = lfu_keys[0]

                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.recency[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.recency[key] = self.time
            self.time += 1

    def get(self, key):
        """
        Get an item by key from the cache.

        Args:
            key (str): The key to look up in the cache.

        Returns:
            any: The item stored under the key/None if the key doesn't exist.
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.recency[key] = self.time
            self.time += 1
            return self.cache_data[key]
        return None

    def lru_discard(self):
        """ LRU Discard helper function """
        lru_key = min(self.recency, key=self.recency.get)
        del self.cache_data[lru_key]
        del self.frequency[lru_key]
        del self.recency[lru_key]
        print(f"DISCARD: {lru_key}")
