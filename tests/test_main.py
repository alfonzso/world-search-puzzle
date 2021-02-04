import unittest
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
"""
]


class TestScript(unittest.TestCase):
    _ws = None

    def base(self, word_search_txt, text_to_search):
        self._ws.gen_word_search_list(word_search_txt)
        self._ws.search_begin(text_to_search)
        self.assertEqual(text_to_search, self._ws.print_result_by_indexes())

    def setup_method(self, test_method):
        self._ws = WordSearcher()

    def teardown_method(self, test_method):
        del self._ws

    def test_search_00(self):
        wst = word_search_txt_list[0][1:]
        text_to_search = "mazsola"

        self.base(wst, text_to_search)

    def test_search_01(self):
        wst = word_search_txt_list[1][1:]
        text_to_search = "mazsola"

        self.base(wst, text_to_search)

    def test_search_02(self):
        wst = word_search_txt_list[2][1:]
        text_to_search = "mazsola"

        self.base(wst, text_to_search)

    def test_search_03(self):
        wst = word_search_txt_list[3][1:]
        text_to_search = "mazsola"

        self.base(wst, text_to_search)
