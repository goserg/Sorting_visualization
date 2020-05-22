from typing import Iterator

from sorters.sorter import Sorter


class ShakerSorter(Sorter):
    name = "Shaker"

    def sort(self) -> Iterator:
        data = self.data_list
        up = range(len(data) - 1)
        while True:
            for indices in (up, reversed(up)):
                swapped = False
                for i in indices:
                    self.compare_counter += 1
                    yield
                    if data[i] > data[i + 1]:
                        color1, color2 = data[i].color, data[i + 1].color
                        data[i].pos, data[i + 1].pos = data[i + 1].pos, data[i].pos
                        data[i], data[i + 1] = data[i + 1], data[i]
                        data[i].color, data[i + 1].color = color2, color1
                        swapped = True
                        self.replacing_counter += 1
                if not swapped:
                    return
