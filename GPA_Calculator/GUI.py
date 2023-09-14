import customtkinter as ctk
from tabulate import tabulate
from pandas import read_excel
from sys import exit

ctk.set_default_color_theme('green')
ctk.set_appearance_mode('System')


class Window(ctk.CTk):
    def __init__(self, df, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("GPA Calculator")
        self.df = df.dropna(axis=0)
        print(tabulate(self.df))
        self.columns = tuple(self.df.columns)
        self.grades = {"EX": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 5, "R": 0}
        self._grades = tuple(self.grades.keys())
        self.res = list()
        self.empty = None
        self.Create()

    def Create(self):
        for i, j in enumerate(self.df[self.columns[0]]):
            self.res.append(ctk.StringVar(self, value='\0'))
            ctk.CTkLabel(self, text=j, font=("Segoe ui semibold", 16)).grid(row=i, column=0, pady=10, padx=20)
            ctk.CTkLabel(self, text=":", font=("Segoe ui semibold", 16)).grid(row=i, column=1, pady=10, padx=5)
            ctk.CTkOptionMenu(self, variable=self.res[i], values=self._grades, command=self.Calculate).grid(row=i,
                                                                                                            column=2,
                                                                                                            pady=10,
                                                                                                            padx=20)
            ctk.CTkLabel(self, text="Total Credits", font=("Segoe ui semibold", 16)).grid(row=i + 1, column=0, pady=10,
                                                                                          padx=20)
            ctk.CTkLabel(self, text=":", font=("Segoe ui semibold", 16)).grid(row=i + 1, column=1, pady=10, padx=5)
            ctk.CTkLabel(self, text=sum(self.df[self.columns[1]]), font=("Segoe ui semibold", 16)).grid(row=i + 1,
                                                                                                        column=2,
                                                                                                        pady=10,
                                                                                                        padx=20)
            ctk.CTkLabel(self, text="Your GPA", font=("Segoe ui semibold", 16)).grid(row=i + 2, column=0, pady=10,
                                                                                     padx=20)
            ctk.CTkLabel(self, text=":", font=("Segoe ui semibold", 16)).grid(row=i + 2, column=1, pady=10, padx=5)
            self.empty = ctk.CTkLabel(self, text='\0', font=("Segoe ui semibold", 16))
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
            self.empty.configure(text=str(_sum / sum(self.df[self.columns[1]])))


class App(ctk.CTk):

    def __init__(self, df, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.df = df
        self.title("Selection Menu")
        self.branches = ("CSE", "ECE", "EEE", "MECH", "CIVIL", "CHEM", "MME")
        self.branch = ctk.StringVar(self, value='\0')
        self.year = ctk.StringVar(self, value='\0')
        self.sem = ctk.StringVar(self, value="\0")
        self.Create()

    def Topclass(self, *args):
        if self.branch.get() != "\0" and self.year.get() != "\0" and self.sem.get() != "\0":
            Window(self.df[self.branch.get()][[self.year.get() + '-' + self.sem.get(), "Credits_" +
                                               self.year.get() + '-' + self.sem.get()]]).mainloop()

    def Create(self):
        ctk.CTkLabel(self, text='Branch', font=("Segoe ui semibold", 16)).grid(row=0, column=0, pady=(50, 20), padx=20)
        ctk.CTkLabel(self, text=':', font=("Segoe ui semibold", 16)).grid(row=0, column=1, pady=(50, 20), padx=5)
        ctk.CTkOptionMenu(self, values=self.branches, dynamic_resizing=False, command=self.Topclass,
                          variable=self.branch).grid(row=0, column=2, pady=(50, 20), padx=20)
        ctk.CTkLabel(self, text="Year", font=("Segoe ui semibold", 16)).grid(row=1, column=0, pady=20, padx=20)
        ctk.CTkLabel(self, text=":", font=("Segoe ui semibold", 16)).grid(row=1, column=1, pady=20, padx=20)
        ctk.CTkOptionMenu(self, values=('E1', 'E2', 'E3', 'E4'), dynamic_resizing=False, command=self.Topclass,
                          variable=self.year).grid(row=1, column=2, pady=20, padx=20)
        ctk.CTkLabel(self, text="Sem", font=("Segoe ui semibold", 16)).grid(row=2, column=0, pady=20, padx=20)
        ctk.CTkLabel(self, text=":", font=("Segoe ui semibold", 16)).grid(row=2, column=1, pady=20, padx=20)
        ctk.CTkOptionMenu(self, values=('S1', 'S2'), variable=self.sem, dynamic_resizing=False,
                          command=self.Topclass).grid(row=2, column=2, pady=20, padx=20)


def get_data(q):
    br = ("CSE", "ECE", "EEE", "MECH", "CIVIL", "CHEM", "MME")
    for i in br:
        q[i] = read_excel('./GPA.xlsx', sheet_name=i)


if __name__ == '__main__':
    Q: dict = dict()
    try:
        get_data(Q)
        App(Q).mainloop()
    except:
        exit(0)
