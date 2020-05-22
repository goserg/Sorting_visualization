from typing import Iterator

from sorters.sorter import Sorter


class InsertionSorter(Sorter):
    name = "Insertion"

    def sort(self) -> Iterator:
        data = self.data_list
        for i in range(1, len(data)):
            item_to_insert = data[i]
            j = i - 1
            while j >= 0 and data[j] > item_to_insert:
                self.compare_counter += 1
                yield
                self.swap(j + 1, j)

                j -= 1
            data[j + 1] = item_to_insert

    def swap(self, i, j):
        data = self.data_list
        color1, color2 = data[i].color, data[j].color
        data[i].pos, data[j].pos = data[j].pos, data[i].pos
        data[i], data[j] = data[j], data[i]
        data[i].color, data[j].color = color2, color1
        self.replacing_counter += 1