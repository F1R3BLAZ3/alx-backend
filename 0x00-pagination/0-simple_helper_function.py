#!/usr/bin/env python3
"""
Pagination Helper

This module provides a function to calculate the start and end indices for a
given page and page size in a 1-indexed pagination system.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing the start index and end index
    for a given page and page size in a 1-indexed pagination system.

    Parameters:
    - page (int): The page number.
    - page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start index and end index.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    # Calculate the start and end indices
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
