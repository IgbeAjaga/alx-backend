#!/usr/bin/env python3
"""Hypermedia pagination sample."""
import csv
import math
from typing import Dict, List, Tuple


def calculate_index_range(page_number: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end index based on page number and page size."""
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class for pagination of popular baby names dataset."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize a new Server instance."""
        self._cached_dataset = None

    def _fetch_dataset(self) -> List[List]:
        """Retrieve and cache the dataset."""
        if self._cached_dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self._cached_dataset = dataset[1:]

        return self._cached_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page of data."""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start_index, end_index = calculate_index_range(page, page_size)
        data = self._fetch_dataset()
        if start_index > len(data):
            return []
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieve information about a page."""
        page_data = self.get_page(page, page_size)
        start_index, end_index = calculate_index_range(page, page_size)
        total_pages = math.ceil(len(self._cached_dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end_index < len(self._cached_dataset) else None,
            'prev_page': page - 1 if start_index > 0 else None,
            'total_pages': total_pages,
        }
        return page_info
