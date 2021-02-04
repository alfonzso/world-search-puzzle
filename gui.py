# import Tkinter as tk
import tkinter as tk

from tkinter import Tk, Canvas, Frame, BOTH, W


data = """
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
papajaefbasdfhnjkléd
úöghjribizlirwdftgái
ertzuaioropnéruhjkln
ertmangósüpnlkletukn
ereuicopőúayioacbety
ananászűücseresznyee
"""


class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # t.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        canvas.create_line(0, 0, 200, 25)


        canvas.create_text(20, 30, anchor=W, font="Purisa",
            text="a")

        # t = SimpleTable(canvas, 10, 5)
        # t.pack(side="top", fill="x")
        # t.pack(fill=BOTH, expand=1)

        canvas.pack(fill=BOTH, expand=1)
        # t.set(0, 0, "Hello, world")


class SimpleTable(tk.Frame):
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


if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
