#!/usr/bin/env python3
"""Hypermedia Pagination"""

from typing import Dict, List, Union
from .1-simple_pagination import Server

class Server(Server):
    """Extended Server class for hypermedia pagination"""

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List[List[Union[str, int]]], None]]:
        """Returns paginated data with metadata"""
        dataset = self.dataset()
        total_pages = len(dataset) // page_size + (len(dataset) % page_size > 0)
        paginated_data = self.get_page(page, page_size)
        next_page = page + 1 if len(paginated_data) == page_size else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(paginated_data),
            "page": page,
            "data": paginated_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
