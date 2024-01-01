#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""
import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance"""
        self._cached_dataset = None
        self._indexed_dataset = None

    def _load_dataset(self) -> List[List]:
        """Loads dataset from file"""
        if self._cached_dataset is None:
            with open(self.DATA_FILE, newline='') as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self._cached_dataset = dataset[1:]
        return self._cached_dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Returns a dataset indexed by sorting position, starting at 0"""
        if self._indexed_dataset is None:
            dataset = self._load_dataset()
            truncated_dataset = dataset[:1000]
            self._indexed_dataset = {
                idx: item for idx, item in enumerate(dataset)
            }
        return self._indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns paginated data with deletion-resilient metadata"""
        data = self.indexed_dataset()
        assert index is not None and 0 <= index <= max(data.keys())
        paginated_data = []
        data_count = 0
        next_index = None
        start = index if index else 0
        for idx, item in data.items():
            if idx >= start and data_count < page_size:
                paginated_data.append(item)
                data_count += 1
                continue
            if data_count == page_size:
                next_index = idx
                break
        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(paginated_data),
            'data': paginated_data,
        }
        return page_info
