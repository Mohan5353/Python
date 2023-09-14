import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Number System Converter")
        self.inp_base = ctk.StringVar(self, value='\0')
        self.inp_val = ctk.StringVar(self, value='\0')
        self.out_base = ctk.StringVar(self, value='\0')
        ctk.CTkLabel(self, text="Base From", font=("Segoe UI semibold", 16)).grid(row=0, column=0, padx=10, pady=20)
        ctk.CTkLabel(self, text=":", font=("Segoe UI semibold", 16)).grid(row=0, column=1, padx=5, pady=20)
        ctk.CTkEntry(self, textvariable=self.inp_base, font=("Segoe UI semibold", 16)).grid(row=0, column=2, padx=10,
                                                                                            pady=20)
        ctk.CTkLabel(self, text="Value", font=("Segoe UI semibold", 16)).grid(row=1, column=0, padx=10, pady=20)
        ctk.CTkLabel(self, text=":", font=("Segoe UI semibold", 16)).grid(row=1, column=1, padx=5, pady=20)
        ctk.CTkEntry(self, textvariable=self.inp_val, font=("Segoe UI semibold", 16)).grid(row=1, column=2, padx=10,
                                                                                           pady=20)
        ctk.CTkLabel(self, text="To Base", font=("Segoe UI semibold", 16)).grid(row=2, column=0, padx=10, pady=20)
        ctk.CTkLabel(self, text=":", font=("Segoe UI semibold", 16)).grid(row=2, column=1, padx=5, pady=20)
        ctk.CTkEntry(self, textvariable=self.out_base, font=("Segoe UI semibold", 16)).grid(row=2, column=2, padx=10,
                                                                                            pady=20)
        ctk.CTkButton(self, text="Convert", font=("Segoe UI semibold", 16), command=self.ToDecimal).grid(row=3,
                                                                                                         column=1,
                                                                                                         pady=20)
        ctk.CTkLabel(self, text="Answer", font=("Segoe UI semibold", 16)).grid(row=4, column=0, padx=10, pady=20)
        ctk.CTkLabel(self, text=":", font=("Segoe UI semibold", 16)).grid(row=4, column=1, padx=5, pady=20)
        self.empty_label = ctk.CTkLabel(self, text='', font=("Segoe UI semibold", 16))
        self.empty_label.grid(row=4, column=2, padx=10, pady=20)
        self.bind("<Return>", func=self.ToDecimal)

    def ToDecimal(self, *args) -> str:
        num = (self.inp_val.get()).upper()
        if (base := int(self.inp_base.get())) != 10:
            dec_val = 0
            if '.' in num:
                num, dec = num.split('.')
                for i, j in enumerate(dec):
                    if j.isalpha():
                        j = str(ord(j) - 55)
                    dec_val += int(j) * (base ** -(i + 1))
            num_val = str(int(num, base=base))
            if dec_val != 0:
                text = num_val + str(dec_val)[1:]
            else:
                text = num_val
            if self.out_base.get() == 10:
                self.empty_label.configure(text=text)
            else:
                self.empty_label.configure(text=self.ToOther(text))
        else:
            self.empty_label.configure(text=self.ToOther(num))

    def ToOther(self, num: str):
        base = int(self.out_base.get())
        res: list[int, ...] = list()
        dec: str = '0'
        dec_val: list[int, ...] = list()
        if '.' in num:
            num, dec = num.split('.')
            dec = float('0.' + dec)
            int_med = []
            while dec not in int_med and dec > 0:
                int_med.append(dec)
                rem = int(dec := (dec * base))
                dec -= rem
                dec_val.append(rem) if rem < 10 else dec_val.append(chr(rem + 55))
        num = int(num)
        while num > 0:
            rem = num % base
            if rem < 10:
                res.insert(0, str(rem))
            else:
                res.insert(0, chr(rem + 55))
            num //= base
        return ''.join(res) if dec == '0' else ''.join(res) + '.' + ''.join(map(str, dec_val))

# App().mainloop()
