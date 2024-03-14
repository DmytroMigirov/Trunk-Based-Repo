import tkinter as tk
import random
import alg as f1
import alg2 as f2


class SimpleTableInput(tk.Frame):
    def __init__(self, parent, rows, columns, check, mass):
        tk.Frame.__init__(self, parent)

        self._entry = {}
        self.rows = rows
        self.columns = columns
        vcmd = (self.register(self._validate), "%P")
        if check is False and mass is None:
            for row in range(self.rows):
                for column in range(self.columns): 
                    index = (row, column)
                    e = tk.Entry(self, validate="key", validatecommand=vcmd)
                    e.grid(row=row, column=column, stick="nsew")
                    self._entry[index] = e
        if check is True and mass is None:
            for row in range(self.rows):
                for column in range(self.columns):
                    index = (row, column)
                    e = tk.Entry(self, validate="key", validatecommand=vcmd)
                    e.grid(row=row, column=column, stick="nsew")
                    e.insert(0, random.randint(1, 20))
                    self._entry[index] = e
        if mass is not None:
            for row in range(self.rows):
                for column in range(self.columns):
                    index = (row, column)
                    e = tk.Entry(self, validate="key", validatecommand=vcmd)
                    e.grid(row=row, column=column, stick="nsew")
                    e.insert(0, float('{:.3f}'.format(mass[row][column])))
                    self._entry[index] = e
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(float(self._entry[index].get()))
            result.append(current_row)
        return result

    def _validate(self, P):
        if P.strip() == "":
            return True

        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.lbl = tk.Label(self, text="Size of matrix")
        self.lbl.pack(side="left")
        self.info = tk.Entry(self, width=4)
        self.info.pack(side="left")
        self.info.insert(0, 2)
        self.btn = tk.Button(self, text="Generate matrix", command=self.on_clicked)
        self.btn.pack(side="left")
        self.btn = tk.Button(self, text="Randomize", command=self.random)
        self.btn.pack(side="left")
        self.table = SimpleTableInput(self, 2, 2, False, None)
        self.table.pack(side="top", fill="both", expand=False)
        self.submit = tk.Button(self, text="Submit", command=self.on_submit)
        self.submit.pack(side="bottom")
        self.submit = tk.Button(self, text="Alg petrification", command=self.alg)
        self.submit.pack(side="bottom")
        self.submit = tk.Button(self, text="Alg cells", command=self.algk)
        self.submit.pack(side="bottom")

    def on_clicked(self):
        self.table.destroy()
        try:
            self.table = SimpleTableInput(self, int(self.info.get()), int(self.info.get()), False, None)
            self.table.pack(side="top", fill="both", expand=False)
        except ValueError:
            print("Invalid input")

    def random(self):
        self.table.destroy()
        try:
            self.table = SimpleTableInput(self, int(self.info.get()), int(self.info.get()), True, None)
            self.table.pack(side="top", fill="both", expand=False)
        except ValueError:
            print("Invalid input")

    def alg(self):
        A = self.table.get()
        A = f1.transpose(A)
        C = f1.inverse(A)
        print(C)

        self.table.destroy()
        try:
            self.table = SimpleTableInput(self, int(self.info.get()), int(self.info.get()), False, C)
            self.table.pack(side="top", fill="both", expand=False)
        except ValueError:
            print("Invalid input")

    def algk(self):
        A = self.table.get()
        result = f2.invert(A)
        self.table.destroy()
        try:
            self.table = SimpleTableInput(self, int(self.info.get()), int(self.info.get()), False, result)
            self.table.pack(side="top", fill="both", expand=False)
        except ValueError:
            print("Invalid input")

    def on_submit(self):
        print(self.table.get())
        A = self.table.get()
        f1 = open('output.txt', 'w')
        for j in A:
            f1.write(str(j))
            f1.write("\n")
        f1.close()


root = tk.Tk()
Example(root).pack(side="top", fill="both", expand=True)
root.mainloop()
