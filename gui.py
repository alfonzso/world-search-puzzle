from main import WordSearcher
from tkinter import *

data = """almatjdatolyawisertm
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

# data = """mazsola
# asdsola
# asdsola
# asdsola
# asdsola
# asdsola
# asdsola
# """


# text_to_search_list = [
#     "görögdinnye",
#     "ananász",
#     "alma",
#     "szőlő",
#     "őszibarack",
#     "sárgadinnye",
#     "szeder",
#     "pocok",
# ]
textbox_text = """görögdinnye
ananász
alma
szőlő
őszibarack
sárgadinnye
szeder
pocok
"""


class ExampleApp(Tk):
    _yn = -1
    _xn = -1
    _match = False
    _col_idx_list = None
    _row_idx_list = None
    _padding = -1
    _padding_step = -1
    _col_padding = -1
    _canvas = None

    def __init__(self):
        Tk.__init__(self)

        self._canvas = Canvas(self)
        self._padding = 0
        self._padding_step = 20
        self._col_padding = 0
        self._col_idx_list = []
        self._row_idx_list = []
        for row_idx, row in enumerate(data.splitlines()):

            self._xn = 10 + len(row) * 35
            self._canvas.create_line(10, 10 + self._padding + row_idx, self._xn, 10 + self._padding + row_idx)
            self._col_idx_list = []
            for cols_idx, column in enumerate(row):
                if not self._match:
                    self._yn = 10 + (22 + len(row) - 1 + (len(row) - 1) * self._padding_step)
                    self._canvas.create_line(10 + cols_idx * 35, 10, 10 + cols_idx * 35, self._yn)
                self._canvas.create_text(20 + cols_idx * 35, 22 + row_idx + self._padding, anchor=W, font="Purisa", text=column)
                self._col_idx_list.append([20 + cols_idx * 35, 22 + row_idx + self._padding])
                self._col_padding += 25

            self._match = True
            self._padding += self._padding_step
            self._row_idx_list.append(self._col_idx_list)

        self._canvas.create_line(10, self._yn, self._xn, self._yn)
        self._canvas.create_line(self._xn, 10, self._xn, self._yn)

        self._canvas.pack(fill=BOTH, expand=1)

    def draw_line(self, x1, y1, x2, y2):
        self._canvas.create_line(x1 + 5, y1, x2 + 5, y2, width=10, fill='green', stipple='gray50')


class TextBox(Text):
    _hei = 50
    _wid = 200
    _max = -1
    _master: ExampleApp = None
    _b = None

    def hello_button(self):

        list_of_text = filter(None,self.get("1.0", END).splitlines())
        for text in list_of_text:
            _ws = WordSearcher()
            _ws.gen_word_search_list(data)
            _ws.search_begin(text)
            result = _ws.print_result_by_indexes()
            print(
                "result:", result
            )
            if not result:
                print("ERROR: %s not found ! " % text)
                break
            data_ws = _ws._idx_pair_list

            fx, fy = data_ws[0]
            lx, ly = data_ws[-1]
            x1, y1 = self._master._row_idx_list[fx][fy]
            x2, y2 = self._master._row_idx_list[lx][ly]
            print(
                "idx: ", x1 + 5, y1, x2 + 5, y2
            )
            self._master.draw_line(x1, y1, x2, y2)

    def __init__(self, master):
        self._master = master
        Text.__init__(self, master)
        self.place(x=master._xn + 10, y=10, height=self._hei, width=self._wid)

        self._b = Button(master, text="Hello", command=self.hello_button)

        self._b.place(x=master._xn + ((self._wid - 32) / 2), y=self._hei + 10)  # height=10, width=10)

        self.bind('<Return>', self.motion)
        self.bind('<BackSpace>', self.neg_motion)

        self._init_textbox_text()

    def _init_textbox_text(self):

        self.insert(INSERT, textbox_text)
        self._max = len(textbox_text.splitlines())

        self._hei = self._hei_step * self._max + self._hei_step

        self.place(x=self._master._xn + 10, y=10, height=self._hei, width=self._wid)
        self._b.place(x=self._master._xn + ((self._wid - 32) / 2), y=self._hei + 10)

    _hei_step = 16

    def motion(self, event):
        self._hei += self._hei_step
        _str = self.get("1.0", END)
        print(
            _str,
            len(_str.splitlines())
        )
        if self._max < len(_str.splitlines()):
            self._max = len(_str.splitlines())

        if len(_str.splitlines()) >= 2:
            self.place(x=self._master._xn + 10, y=10, height=self._hei, width=self._wid)
            self._b.place(x=self._master._xn + ((self._wid - 32) / 2), y=self._hei + 10)
        print("Mouse position: (%s %s)" % (event.x, event.y))
        return

    def neg_motion(self, event):
        _str = self.get("1.0", END)
        print(
            _str,
            len(_str.splitlines())
        )
        if self._max > len(_str.splitlines()):
            self._hei -= 12.5
            self._max = len(_str.splitlines())
            self.place(x=self._master._xn + 10, y=10, height=self._hei, width=self._wid)
            self._b.place(x=self._master._xn + ((self._wid - 32) / 2), y=self._hei + 10)
        return


if __name__ == "__main__":
    app = ExampleApp()
    tb = TextBox(app)
    wid = 200
    app.geometry('%dx%d' % (app._xn + 10 + wid + 5, app._yn + 10))
    app.mainloop()
