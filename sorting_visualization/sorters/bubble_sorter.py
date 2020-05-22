from typing import Iterator

from sorters.sorter import Sorter


class BubbleSorter(Sorter):
    name = "Bubble"

    def sort(self) -> Iterator:
        data = self.data_list
        for i in range(len(data) - 1):
            for j in range(len(data) - i - 1):
                self.compare_counter += 1
                yield
                if data[j] > data[j + 1]:
                    color1, color2 = data[j].color, data[j + 1].color
                    data[j].pos, data[j + 1].pos = data[j + 1].pos, data[j].pos
                    data[j], data[j + 1] = data[j + 1], data[j]
                    data[j].color, data[j + 1].color = color2, color1
                    self.replacing_counter += 1
