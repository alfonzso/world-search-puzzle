
import math


class WordSearcher(object):

    _word_search_list = None
    _word_search_txt = None
    _idx_pair_list = None
    _idx_distance_list = None

    _match = False

    def _wst_init__(self, __word_search_txt) -> None:
        self._word_search_txt = __word_search_txt
        self._word_search_list = [["" for i in range(len(__word_search_txt.splitlines()[0]))] for j in range(len(__word_search_txt.splitlines()))]
        self._idx_pair_list = []
        self._idx_distance_list = []

    def remove_none(self, _list):
        a = []
        for x in _list:
          for y in x:
            if y:
                a.append(y)
        return a

    def gen_word_search_list(self, _word_search_txt):
        self._wst_init__(_word_search_txt)
        for idx_x, line in enumerate(self._word_search_txt.splitlines()):
            _tmp_list = []
            for idx_y, char in enumerate(line):
                self._word_search_list[idx_x][idx_y] = char

    def get_neighbours(self, x, y):
        final_top = []
        for i in range(-1, 2):
            left = [x + i, y - 1]
            middle = [x + i, y]
            right = [x + i, y + 1]
            if not (left[0] >= 0 and left[1] >= 0):
                left = None
            if not (middle[0] >= 0 and middle[1] >= 0) or i == 0:
                middle = None
            if not (right[0] >= 0 and right[1] >= 0):
                right = None
            final_top.append([left, middle, right])
        return final_top

    def get_neighbours_arranged(self, x, y):
        top = self.remove_none(self.get_neighbours(x, y))
        return top

    def found_first_char(self):
        found_msg = None
        found = []
        for idx_x, i in enumerate(self._word_search_list):
            for idx_y, x in enumerate(i):
                print(
                    x, end=", "
                )
                if self._text_to_search[0] == x:
                    found_msg = "found first char %d:%d" % (idx_x, idx_y)
                    found.append([idx_x, idx_y])
            print()
        print(found_msg)
        return found

    def print_result_by_indexes(self):
        result_string = ""
        for idx_pair in self._idx_pair_list:
            x, y = idx_pair
            result_string += self._word_search_list[x][y]
        return result_string

    def search_begin(self, __text_to_search):
        self._text_to_search = __text_to_search
        founds = self.found_first_char()
        for found in founds:
            self.search_match(found, 1)
            print(
                self._idx_pair_list
            )
            if self._match:
                break

    @staticmethod
    def colliniear(ax, ay, bx, by, cx, cy):
        return ax * (by - cy) + bx * (cy - ay) + cx * (ay - by) == 0

    def len_is_ok(self, x):
        return x < len(self._word_search_list)

    def is_collinear(self, x, y):
        return self.colliniear(*self._idx_pair_list[0], *self._idx_pair_list[1], x, y)

    @staticmethod
    def distance(a, b):
        ax, ay = a
        bx, by = b
        return math.sqrt((ax - bx)**2 + (ay - by)**2)

    def search_match(self, current_idx_pair, letter_idx):

        self._idx_pair_list.append(current_idx_pair)
        for x, y in self.get_neighbours_arranged(*current_idx_pair):
            if self.len_is_ok(x) and \
               self.len_is_ok(y) and \
               self._word_search_list[x][y] == self._text_to_search[letter_idx]:
                if letter_idx > 2 and self.is_collinear(x, y):
                    _distance = self.distance(self._idx_pair_list[0], [x, y])
                    if len(self._idx_distance_list) != 0:
                        if self._idx_distance_list[-1] > _distance:
                            continue

                    self._idx_distance_list.append(_distance)

                    print("->" * letter_idx, x, y, self._word_search_list[x][y])
                    if letter_idx + 1 < len(self._text_to_search):
                        self._match = self.search_match([x, y], letter_idx + 1)
                    else:
                        self._idx_pair_list.append([x, y])
                        return True
                if letter_idx <= 2 and not self._match:
                    print("->" * letter_idx, x, y, self._word_search_list[x][y])
                    if letter_idx + 1 < len(self._text_to_search):
                        self._match = self.search_match([x, y], letter_idx + 1)
        if not self._match:
            self._idx_pair_list.pop()
            if len(self._idx_distance_list) != 0:
                self._idx_distance_list.pop()
        pass
        return self._match
