#!/usr/bin/env python3
"""Simple Pagination"""

import csv
from typing import List, Union

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[Union[str, int]]]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='') as file:
                reader = csv.reader(file)
                self.__dataset = list(reader)[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[Union[str, int]]]:
        """Returns paginated data"""
        dataset = self.dataset()
        start = (page - 1) * page_size
        end = start + page_size
        return dataset[start:end]
