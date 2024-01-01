#!/usr/bin/env python3
"""Simple pagination sample."""

import csv
from typing import List, Tuple


def calculate_index_range(page_number: int, size: int) -> Tuple[int, int]:
    """Calculates the index range based on the page number and size."""
    start_index = (page_number - 1) * size
    end_index = start_index + size
    return start_index, end_index


class Server:
    """Server class for paginating a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize a new Server instance."""
        self._cached_data = None

    def _fetch_dataset(self) -> List[List]:
        """Retrieve and cache the dataset."""
        if self._cached_data is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self._cached_data = dataset[1:]

        return self._cached_data

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page of data."""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start_index, end_index = calculate_index_range(page, page_size)
        data = self._fetch_dataset()
        if start_index > len(data):
            return []
        return data[start_index:end_index]
