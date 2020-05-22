from typing import Iterator

from sorters.sorter import Sorter


class SelectionSorter(Sorter):
    name = "Selection"

    def sort(self) -> Iterator:
        data = self.data_list
        for i in range(len(data)):
            lowest_value_index = i
            for j in range(i + 1, len(data)):
                yield
                self.compare_counter += 1
                if data[j] < data[lowest_value_index]:
                    lowest_value_index = j
            color1, color2 = data[i].color, data[lowest_value_index].color
            data[i].pos, data[lowest_value_index].pos = data[lowest_value_index].pos, data[i].pos
            data[i], data[lowest_value_index] = data[lowest_value_index], data[i]
            data[i].color, data[lowest_value_index].color = color2, color1
            self.replacing_counter += 1
