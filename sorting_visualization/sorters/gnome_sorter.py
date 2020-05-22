from typing import Iterator

from sorters.sorter import Sorter


class GnomeSorter(Sorter):
    name = "Gnome"

    def sort(self) -> Iterator:
        data = self.data_list
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(data) - 1):
                self.compare_counter += 1
                yield
                if data[i] > data[i + 1]:
                    is_sorted = False
                    color1, color2 = data[i].color, data[i + 1].color
                    data[i].pos, data[i + 1].pos = data[i + 1].pos, data[i].pos
                    data[i], data[i + 1] = data[i + 1], data[i]
                    data[i].color, data[i + 1].color = color2, color1
                    self.replacing_counter += 1
                    break
