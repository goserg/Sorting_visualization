import time
from typing import List, Any, Iterator
from abc import ABC, abstractmethod


class Sorter(ABC):
    name = "A sort"

    def __init__(self, data_list: List[Any]) -> None:
        self.data_list = data_list[:]
        self.replacing_counter = 0
        self.compare_counter = 0
        self.start_time = time.time()
        self.iterator = self.sort()

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> None:
        try:
            next(self.iterator)
        except StopIteration:
            print(f"{self.name} finished in {time.time() - self.start_time:.2f} second(s)")
            print(f"total of {self.compare_counter} compares and {self.replacing_counter} replaces")
            raise StopIteration

    @abstractmethod
    def sort(self) -> Iterator:
        """iterator"""
