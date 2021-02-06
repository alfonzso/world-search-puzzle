# import Tkinter as tk
from main import WordSearcher
# import tkinter as tk

# from tkinter import Tk, Canvas, Frame, BOTH, W

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


class ExampleApp(Tk):
    _yn = -1
    _xn = -1

    def __init__(self):
        Tk.__init__(self)

        # t.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        # canvas.create_line(0, 0, 200, 25)
        # canvas.create_line(1, 10, 200, 10)
        # canvas.create_line(1, 20, 200, 20)
        # canvas.create_line(1, 30, 200, 30)
        padding = 0
        padding_step = 20
        col_padding = 0
        t_row_idx = 1
        t_cols_idx = 1
        match = False
        # self._yn = -1
        # self._xn = -1
        # canvas.create_line(10, 15, 10, 310)
        # canvas.create_line(20, 15, 20, 310)
        col_idx_list = None
        row_idx_list = []
        for row_idx, row in enumerate(data.splitlines()):

            # current_row = []
            # canvas.create_line(10, row_idx + padding, 310, row_idx + padding)
            # print(
            #     10 +  len(row)  * 35
            # )
            self._xn = 10 + len(row) * 35
            canvas.create_line(10, 10 + padding + row_idx, self._xn, 10 + padding + row_idx)

            # print(
            #     10 + padding + row_idx, 10 + (padding_step * len(data.splitlines())) + padding_step
            # )
            col_idx_list = []
            for cols_idx, column in enumerate(row):

                # canvas.create_line(cols_idx + col_padding, 15, cols_idx + col_padding, 310)
                # t_row_idx = row_idx * 2 + 22
                # t_cols_idx = cols_idx * 20 + 6
                if not match:
                    # canvas.create_line(10 + (col_padding + row_idx) * 1.2, 10, 10 + (col_padding + row_idx) * 1.2, 430)
                    # canvas.create_line(10 + (col_padding) * 1.2, 10, 10 + (col_padding) * 1.2, 430)
                    self._yn = 10 + (22 + len(row) - 1 + (len(row) - 1) * padding_step)
                    # canvas.create_line(10 + cols_idx * 35, 10, 10 + cols_idx * 35, 10 + (padding_step * len(data.splitlines())) + padding_step)
                    canvas.create_line(10 + cols_idx * 35, 10, 10 + cols_idx * 35, self._yn)
                    # print(
                    #     10 + cols_idx * 35, 10, 10 + cols_idx * 35, 430
                    # )
                    # print(
                    #     10 + cols_idx * 35, "--->"
                    # )
                    # canvas.create_line(10 + t_row_idx, 15, 10 + t_cols_idx, 420)
                # t_row_idx = padding * 2 + 22
                # t_cols_idx = padding * 20 + 3.5
                # t_row_idx = t_row_idx * 2 + 22
                # t_cols_idx = t_cols_idx * 20 + 3.5
                # cols_idx**
                # print(
                #     cols_idx + col_padding, "---->", cols_idx + col_padding
                # )
                # canvas.create_text(10+t_cols_idx, t_row_idx, anchor=W, font="Purisa", text="a")
                # canvas.create_text(10 + t_cols_idx, t_row_idx + padding, anchor=W, font="Purisa", text=column)
                # canvas.create_text(10 + t_cols_idx, 22+ row_idx + padding, anchor=W, font="Purisa", text=column)
                # canvas.create_text(10 + t_cols_idx * 1.19, 22 + row_idx + padding, anchor=W, font="Purisa", text=column)
                canvas.create_text(20 + cols_idx * 35, 22 + row_idx + padding, anchor=W, font="Purisa", text=column)
                # print(
                #     20 + cols_idx * 35, 22 + row_idx + padding
                # )
                col_idx_list.append([20 + cols_idx * 35, 22 + row_idx + padding])
                # print(
                #     "======>", 20 + cols_idx * 35, 22 + row_idx + padding, row_idx, padding, 22 + len(row) - 1 + (len(row) - 1) * padding_step
                # )
                # 22+  len(row) -1 + (len(row) -1) * padding_step
                # (22 + (len(row) - 1) + (padding * (len(row) - 1)))
                # canvas.create_text(8 + t_cols_idx, t_row_idx , anchor=W, font="Purisa", text=column)
                # canvas.create_text(8 * 20 + 3.5, padding * 2 + 22, anchor=W, font="Purisa", text=column)
                # canvas.create_text(t_row_idx, t_cols_idx, anchor=W, font="Purisa", text="a")
                col_padding += 25

            match = True
            padding += padding_step
            row_idx_list.append(col_idx_list)

        # canvas.create_line(10, 430, 455, 430)
        # canvas.create_line(455, 10, 455, 430)
        # 10 + ( 7 * 20 ) + 20  = 170 ==> 158 // 12
        # 10 + ( 20 * 10 ) + 20 = 430 ==> 430
        # yn = 10 + (padding_step * len(data.splitlines())) + padding_step
        # yn = 10 + (22 + len(row) - 1 + (len(row) - 1) * padding_step)
        # print(yn)
        # yn = 158
        canvas.create_line(10, self._yn, self._xn, self._yn)
        canvas.create_line(self._xn, 10, self._xn, self._yn)

        # canvas.create_text(20, 30, anchor=W, font="Purisa", text="a")

        # t = SimpleTable(canvas, 10, 5)
        # t.pack(side="top", fill="x")
        # t.pack(fill=BOTH, expand=1)

        canvas.pack(fill=BOTH, expand=1)

        # print(
        #     row_idx_list
        # )

        # text_to_search = "görögdinnye"
        # text_to_search = "ananász"
        text_to_search_list = [
            "görögdinnye",
            "ananász",
            "alma",
            "szőlő",
            "őszibarack",
            "sárgadinnye",
            "szeder",
            "pocok",
        ]
        for text in text_to_search_list:
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
            x1, y1 = row_idx_list[fx][fy]
            x2, y2 = row_idx_list[lx][ly]
            print(
                "idx: ", x1 + 5, y1, x2 + 5, y2
            )
            canvas.create_line(x1 + 5, y1, x2 + 5, y2, width=10, fill='green', stipple='gray50')
        # t.set(0, 0, "Hello, world")


class SimpleTable(Frame):
    def __init__(self, parent, rows=10, columns=2):
        # use black background so it "peeks through" to
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        # for row in range(rows):
        #     current_row = []
        #     for column in range(columns):
        #         label = tk.Label(self, text="%s/%s" % (row, column), borderwidth=0, width=10)
        #         label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
        #         current_row.append(label)
        #     self._widgets.append(current_row)

        # for column in range(columns):
        #     self.grid_columnconfigure(column, weight=1)

        for row_idx, row in enumerate(data.splitlines()):
            current_row = []
            for cols_idx, column in enumerate(row):
                label = tk.Label(self, text="%s" % column, borderwidth=0, width=2)
                label.grid(row=row_idx, column=cols_idx, sticky="nsew", padx=1, pady=1)
                # label.grid(row=row_idx, column=cols_idx, sticky="W", pady=2)
                # label.grid(row=row_idx, column=cols_idx, )
                current_row.append(label)
            self._widgets.append(current_row)

        for row_idx, row in enumerate(data.splitlines()):
            self.grid_rowconfigure(row_idx, weight=1)
            for cols_idx, column in enumerate(row):
                self.grid_columnconfigure(cols_idx, weight=1)

        # self._widgets.append(canvas)
        # canvas.pack(fill=BOTH, expand=1)
        # self.grid_rowconfigure(0, weight=0, uniform='row')
        # self.grid_columnconfigure(0, weight=0, uniform='row')

    # def set(self, row, column, value):
    #     widget = self._widgets[row][column]
    #     widget.configure(text=value)


class TextBox(Text):
    _hei = 50
    _wid = 200
    _max = -1
    _master = None
    _b = None

    def hello_button(self):

        print("hellllllllllla")
        print(
            self._b.winfo_width()
        )

    def __init__(self, master):
        self._master = master
        Text.__init__(self, master)
        self.place(x=master._xn + 10, y=10, height=self._hei, width=self._wid)

        self._b = Button(master, text="Hello", command=self.hello_button)

        # b.place(x=master._xn + 10, y=10, height=self._hei + 10, width=self._wid)
        self._b.place(x=master._xn + ((self._wid - 32) / 2), y=self._hei + 10)  # height=10, width=10)

        self.bind('<Return>', self.motion)
        self.bind('<BackSpace>', self.neg_motion)

    def motion(self, event):
        # T.set
        # global hei
        # global _max
        # print(T.winfo_width)
        # self._hei += 12.5
        self._hei += 16
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
        # T.set
        # global hei
        # global _max
        # print(T.winfo_width)

        _str = self.get("1.0", END)
        print(
            _str,
            len(_str.splitlines())
        )
        if self._max > len(_str.splitlines()):
            self._hei -= 12.5
            _max = len(_str.splitlines())
            self.place(x=self._master._xn + 10, y=10, height=self._hei, width=self._wid)
            self._b.place(x=self._master._xn + ((self._wid - 32) / 2), y=self._hei + 10)
        # print("Mouse position: (%s %s)" % (event.x, event.y))
        return


if __name__ == "__main__":
    app = ExampleApp()
    # app.geometry('460x460')

    tb = TextBox(app)

    # T = Text(app)  # , height=2, width=30, )  # command=spinbox1_callback)
    # T.set
    # hei = 50
    wid = 200
    # T.place(x=app._xn + 10, y=10, height=hei, width=wid)

    app.geometry('%dx%d' % (app._xn + 10 + wid + 5, app._yn + 10))

    app.mainloop()
