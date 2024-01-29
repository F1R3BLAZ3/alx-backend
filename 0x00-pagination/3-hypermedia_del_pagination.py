#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with pagination information
        based on the provided index.

        Parameters:
        - index (int): The current start index of the return page.
          Default is None.
        - page_size (int): The current page size. Default is 10.

        Returns:
        Dict: A dictionary containing pagination information.
        """
        assert index is None or (isinstance(
            index, int) and
            index >= 0
        ), "Index must be None or a non-negative integer."
        assert (
            isinstance(page_size, int)
            and page_size > 0
        ), "Page size must be a positive integer."

        dataset = self.dataset()
        total_items = len(dataset)

        if index is None:
            index = 0
        else:
            assert index < total_items, "Index out of range."

        current_page = index // page_size
        start_index = current_page * page_size
        end_index = min(start_index + page_size, total_items)

        next_index = end_index

        page_data = dataset[start_index:end_index]

        return {
            "index": start_index,
            "next_index": next_index,
            "page_size": len(page_data),
            "data": page_data
        }
