import unittest
from unittest.case import expectedFailure
from main import WordSearcher

word_search_txt_list = [
    """
msdfasd
aadfasd
aszfasd
asdsasd
asdsoas
asdsold
asdsola
""",
    """
asdsola
asdsold
asdsoas
asdsasd
aszfasd
aadfasd
msdfasd
""",
    """
msdsola
asdsola
zsdsola
ssdsola
osdsola
lsdsola
asdsola
""",
    """
asdsola
aldsola
asosola
asdsola
asdszla
asdsoaa
asdsolm
""",
    """
mazsola
asdsola
asdsola
asdsola
asdsola
asdsola
asdsola
""",

    """
almatjdatolyawisertm
asdfghihjkeperlzacba
íyxcvbónmqertzueiopn
szőlőszibarackadfghd
zetfhjklékörteéeíyxa
idvbodzabbasdgfrgghr
lertzudviahjkrlékivi
vipasdfggnhjkeéróopn
avokádósmálnasumksré
esmxcdfgenhgjkléuáűs
röeüőáltgfaöertzsuiá
erluiopkgdtruiolzafr
öüoődyxvymköwamcbebg
fráfonyasárgabaracka
papajaefbasdfhnjklkd
úöghjribizlirwdftgoi
ertzuaioropnéruhjkcn
ertmangósüpnlkletuon
ereuicopőúayioacbepy
ananászűücseresznyee
"""
]

#     """
# almatjdatolyawisertg
# asdfghihjkeperlzacbö
# íyxcvbónmqertzueiopr
# szőlőszibarackadfghö
# zetfhjklékörteéeíyxg
# idvbodzabbasdgfrgghr
# lertzudviahjkrlékivi
# vipasdfggnhjkeéróopn
# avokádósmálnasumksré
# esmxcdfgenhgjkléuáűs
# röeüőáltgfaöertzsuiá
# erluiopkgdtruiolzafr
# öüoődyxvymköwamcbebg
# fráfonyasárgabaracka
# papajaefbasdfhnjkléd
# úöghjribizlirwdftgái
# ertzuaioropnéruhjkln
# ertmangósüpnlkletukn
# ereuicopőúayioacbety
# ananászűücseresznyee
# """


class TestScript(unittest.TestCase):
    _ws = None

    def base(self, word_search_txt, expected_idx_pair_list, text_to_search):
        self._ws.gen_word_search_list(word_search_txt)
        self._ws.search_begin(text_to_search)
        result = self._ws.print_result_by_indexes()
        print(
            result
        )
        self.assertEqual(text_to_search, self._ws.print_result_by_indexes())
        if expected_idx_pair_list:
            self.assertEqual(expected_idx_pair_list, self._ws._idx_pair_list)

    def setup_method(self, test_method):
        self._ws = WordSearcher()

    def teardown_method(self, test_method):
        del self._ws

    def test_get_neighbour_idx(self):

        _x = 0
        _y = 0
        r = self._ws.get_neighbours(_x, _y)
        print()
        for x in r:
            for y in x:
                if y is None:
                    y = " None "
                print(y, end=' | ')
            print()

    def test_search_00(self):
        wst = word_search_txt_list[0][1:]
        text_to_search = "mazsola"
        expected_idx_pair_list = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
        self.base(wst, expected_idx_pair_list, text_to_search)

    def test_search_01(self):
        wst = word_search_txt_list[1][1:]
        text_to_search = "mazsola"

        expected_idx_pair_list = [[6, 0], [5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [0, 6]]
        self.base(wst, expected_idx_pair_list, text_to_search)

    def test_search_02(self):
        wst = word_search_txt_list[2][1:]
        text_to_search = "mazsola"

        expected_idx_pair_list = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]
        self.base(wst, expected_idx_pair_list, text_to_search)

    def test_search_03(self):
        wst = word_search_txt_list[3][1:]
        text_to_search = "mazsola"

        expected_idx_pair_list = [[6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]
        self.base(wst, expected_idx_pair_list, text_to_search)

    def test_search_04(self):
        wst = word_search_txt_list[4][1:]
        text_to_search = "mazsola"

        expected_idx_pair_list = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6]]
        self.base(wst, expected_idx_pair_list, text_to_search)

    def test_search_gorog(self):
        wst = word_search_txt_list[5][1:]
        text_to_search = "görögdinnye"

        expected_idx_pair_list = [[9, 11], [10, 11], [11, 11], [12, 11], [13, 11], [14, 11], [15, 11], [16, 11], [17, 11], [18, 11], [19, 11]]
        self.base(wst, expected_idx_pair_list, text_to_search)

    def test_search_alma(self):
        wst = word_search_txt_list[5][1:]
        text_to_search = "alma"

        expected_idx_pair_list = [[0, 0], [0, 1], [0, 2], [0, 3]]
        self.base(wst, expected_idx_pair_list, text_to_search)

    def test_search_szolo(self):
        wst = word_search_txt_list[5][1:]
        text_to_search = "szőlő"

        expected_idx_pair_list = [[3, 0], [3, 1], [3, 2], [3, 3], [3, 4]]
        self.base(wst, expected_idx_pair_list, text_to_search)

    def test_search_pocok(self):
        wst = word_search_txt_list[5][1:]
        text_to_search = "pocok"

        expected_idx_pair_list = [[18, 18], [17, 18], [16, 18], [15, 18], [14, 18]]
        self.base(wst, expected_idx_pair_list, text_to_search)
