#!/usr/bin/env python3
"""Deletion-resilient Hypermedia Pagination"""

from typing import Dict, List, Union

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    # ... (rest of the Server class)
    # Implementation similar to previous tasks

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Union[int, List[List[Union[str, int]]]]]:
        """Returns paginated data with deletion-resilient metadata"""
        if index is None:
            index = 0

        dataset = self.dataset()
        total_pages = len(dataset) // page_size + (len(dataset) % page_size > 0)
        paginated_data = dataset[index:index + page_size]
        next_index = index + page_size if len(paginated_data) == page_size else None

        return {
            "index": index,
            "data": paginated_data,
            "page_size": len(paginated_data),
            "next_index": next_index
        }
