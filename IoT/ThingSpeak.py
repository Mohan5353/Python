from requests import get
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme('green')

write_api = "5MV44BZVPDCQHW7X"


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Controller")
        self.b = list()
        self.b.append(ctk.CTkButton(self, text='Up', font=("Segoe UI semibold", 16),
                                    width=150, height=50))
        self.b[0].grid(row=0, column=1, padx=20, pady=20)
        self.b.append(ctk.CTkButton(self, text='Left', font=("Segoe UI semibold", 16),
                                    width=150, height=50))
        self.b[1].grid(row=1, column=0, padx=20, pady=20)
        self.b.append(ctk.CTkButton(self, text='Right', font=("Segoe UI semibold", 16),
                                    width=150, height=50))
        self.b[2].grid(row=1, column=2, padx=20, pady=20)
        self.b.append(ctk.CTkButton(self, text='Down', font=("Segoe UI semibold", 16),
                                    width=150, height=50))
        self.b[3].grid(row=2, column=1, padx=20, pady=20)
        self.bind("w", func=lambda event: self.change(1))
        self.bind("a", func=lambda event: self.change(2))
        self.bind("d", func=lambda event: self.change(3))
        self.bind("s", func=lambda event: self.change(4))
        self.bind("<Control-w>", func=lambda event: self.change(-1))
        self.bind("<Control-a>", func=lambda event: self.change(-2))
        self.bind("<Control-d>", func=lambda event: self.change(-3))
        self.bind("<Control-s>", func=lambda event: self.change(-4))

    def change(self, i, *val):
        if i > 0:
            while True:
                print(i)
                if (get(url=f"https://api.thingspeak.com/update?api_key={write_api}&field{i}=1").json()) == 0:
                    break
                self.after(50)
            eval(f"self.b[{i - 1}].configure(fg_color='red')")
        else:
            while True:
                print(i)
                if (get(f"https://api.thingspeak.com/update?api_key={write_api}&field{-i}=0").json()) == 0:
                    break
                self.after(50)
            eval(f"self.b[{-i - 1}].configure(fg_color='green')")


if __name__ == "__main__":
    App().mainloop()
