import tkinter as tk
from pandas import read_excel
from sys import exit


class Window(tk.Tk):
    def __init__(self, df, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("GPA Calculator")
        self.df = df.dropna(axis=0)
        self.columns = tuple(self.df.columns)
        self.grades = {"EX": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 5, "R": 0}
        self._grades = tuple(self.grades.keys())
        self.res = list()
        self.empty = None
        self.Create()

    def Create(self):
        for i, j in enumerate(self.df[self.columns[0]]):
            self.res.append(tk.StringVar(self, value='\0'))
            tk.Label(self, text=j, font=("Segoe ui semibold", 16)).grid(row=i, column=0, pady=10, padx=20)
            tk.Label(self, text=":", font=("Segoe ui semibold", 16)).grid(row=i, column=1, pady=10, padx=5)
            tk.OptionMenu(self, self.res[i], *self._grades, command=self.Calculate).grid(row=i,
                                                                                         column=2,
                                                                                         pady=10,
                                                                                         padx=20)
            tk.Label(self, text="Total Credits", font=("Segoe ui semibold", 16)).grid(row=i + 1, column=0, pady=10,
                                                                                      padx=20)
            tk.Label(self, text=":", font=("Segoe ui semibold", 16)).grid(row=i + 1, column=1, pady=10, padx=5)
            tk.Label(self, text=str(sum(self.df[self.columns[1]])), font=("Segoe ui semibold", 16)).grid(row=i + 1,
                                                                                                         column=2,
                                                                                                         pady=10,
                                                                                                         padx=20)
            tk.Label(self, text="Your GPA", font=("Segoe ui semibold", 16)).grid(row=i + 2, column=0, pady=10,
                                                                                 padx=20)
            tk.Label(self, text=":", font=("Segoe ui semibold", 16)).grid(row=i + 2, column=1, pady=10, padx=5)
            self.empty = tk.Label(self, text='\0', font=("Segoe ui semibold", 16))
            self.empty.grid(row=i + 2, column=2, pady=10, padx=20)

    def Calculate(self, *args):
        count = 0
        for i in self.res:
            if i.get() == "\0":
                count += 1
        if count == 0:
            _sum = 0
            for i, j in enumerate(self.res):
                _sum += self.grades[j.get()] * self.df[self.columns[1]][i]
            self.empty.config(text=str(_sum / sum(self.df[self.columns[1]])))


class App(tk.Tk):

    def __init__(self, df, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.df = df
        self.title("Selection Menu")
        self.branches = ("CSE", "ECE", "EEE", "MECH", "CIVIL", "CHEM", "MME")
        self.branch = tk.StringVar(self, value='\0')
        self.year = tk.StringVar(self, value='\0')
        self.sem = tk.StringVar(self, value="\0")
        self.Create()

    def Topclass(self, *args):
        if self.branch.get() != "\0" and self.year.get() != "\0" and self.sem.get() != "\0":
            Window(self.df[self.branch.get()][[self.year.get() + '-' + self.sem.get(), "Credits_" +
                                               self.year.get() + '-' + self.sem.get()]]).mainloop()

    def Create(self):
        tk.Label(self, text='Branch', font=("Segoe ui semibold", 16)).grid(row=0, column=0, pady=(50, 20), padx=20)
        tk.Label(self, text=':', font=("Segoe ui semibold", 16)).grid(row=0, column=1, pady=(50, 20), padx=5)
        tk.OptionMenu(self, self.branch, *self.branches, command=self.Topclass).grid(row=0, column=2, pady=(50, 20),
                                                                                     padx=20)
        tk.Label(self, text="Year", font=("Segoe ui semibold", 16)).grid(row=1, column=0, pady=20, padx=20)
        tk.Label(self, text=":", font=("Segoe ui semibold", 16)).grid(row=1, column=1, pady=20, padx=20)
        tk.OptionMenu(self, self.year, "", 'E1', 'E2', 'E3', 'E4', command=self.Topclass).grid(row=1, column=2,
                                                                                               pady=20, padx=20)
        tk.Label(self, text="Sem", font=("Segoe ui semibold", 16)).grid(row=2, column=0, pady=20, padx=20)
        tk.Label(self, text=":", font=("Segoe ui semibold", 16)).grid(row=2, column=1, pady=20, padx=20)
        tk.OptionMenu(self, self.sem, "", 'S1', 'S2', command=self.Topclass).grid(row=2, column=2, pady=20, padx=20)


def get_data(q):
    br = ("CSE", "ECE", "EEE", "MECH", "CIVIL", "CHEM", "MME")
    for i in br:
        q[i] = read_excel('GPA.xlsx', sheet_name=i)


if __name__ == '__main__':
    Q: dict = dict()
    try:
        get_data(Q)
        App(Q).mainloop()
    except:
        exit(0)
