
class WordSearcher(object):

    _word_search_list = None
    _idx_pair_list = None

    def __init__(self) -> None:
        super().__init__()
        self._word_search_list = [["" for i in range(7)] for j in range(7)]
        self._idx_pair_list = []

    def remove_none(self, _list):
        a = []
        for x in _list:
            if x:
                a.append(x)
        return a

    def gen_word_search_list(self, _word_search_txt):
        for idx_x, line in enumerate(_word_search_txt.splitlines()):
            # print(line)
            for idx_y, char in enumerate(line):
                # print(char, idx_x, idx_y)
                # print(
                #     char, idx_x, idx_y, end=", "
                # )
                self._word_search_list[idx_x][idx_y] = char
            # lineResult = libLAPFF.parseLine(line)
            # print()

    # print(
    #     word_search_list
    # )
    # print()

    def get_neighbour_idx(self, x, y):
        final_top = []
        # top = []
        for i in range(-1, 2):
            # print(i)
            left = [x + i, y - 1]
            middle = [x + i, y]
            right = [x + i, y + 1]
            if not (left[0] >= 0 and left[1] >= 0):
                left = None
            if not (middle[0] >= 0 and middle[1] >= 0) or i == 0:
                middle = None
            if not (right[0] >= 0 and right[1] >= 0):
                right = None
            top = [left, middle, right]
            # top.append([left, middle, right])
            # print(top)
            # top = [[x for x in i if x] for i in top]
            top = self.remove_none(top)
            top = [i for i in top if i]
            final_top.extend(top)
            # top = list(filter(None, i for i in top))
        # final_top = [ i for i in final_top ]
        return final_top

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
                    found = [idx_x, idx_y]
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
        found = self.found_first_char()
        self.search_match(found, 1)
        print(
            self._idx_pair_list
        )

    def colliniear(self, ax, ay, bx, by, cx, cy):
        return ax * (by - cy) + bx * (cy - ay) + cx * (ay - by) == 0


    def len_is_ok(self, x):
        return x < len(self._word_search_list)

    def search_match(self, current_idx_pair, letter_idx):

        match = False
        self._idx_pair_list.append(current_idx_pair)
        for x, y in self.get_neighbour_idx(*current_idx_pair):
            # print("->" * letter_idx, x, y, word_search_list[x][y])
            if self.len_is_ok(x) and self.len_is_ok(y) and self._word_search_list[x][y] == self._text_to_search[letter_idx]:
                # if word_search_list[x][y] == text_to_search[letter_idx]:
                # letter_idx+1

                if letter_idx > 2 and self.colliniear(*self._idx_pair_list[0], *self._idx_pair_list[1], x, y):
                    print("->" * letter_idx, x, y, self._word_search_list[x][y])
                    if letter_idx + 1 < len(self._text_to_search):
                        match = self.search_match([x, y], letter_idx + 1)
                    else:
                        self._idx_pair_list.append([x, y])
                        return True
                if letter_idx <= 2 and not match:
                    print("->" * letter_idx, x, y, self._word_search_list[x][y])
                    if letter_idx + 1 < len(self._text_to_search):
                        match = self.search_match([x, y], letter_idx + 1)
        # if letter_idx + 1 < len(text_to_search)-1:
        if not match:
            # print(letter_idx + 1 , len(text_to_search))
            # print(idx_pair_list)
            self._idx_pair_list.pop()
        pass
        return match

