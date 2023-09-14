from customtkinter import *
from Number_System_Converter import App
from Temp_Cleaner import Temp_clean
from File_Organizer import File_organizer

set_appearance_mode("System")
set_default_color_theme("green")


class main(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Main")
        self.geometry("350x250")
        CTkLabel(self, text="Choose Operation", font=('Arial', 14)).pack(padx=10, pady=10)
        CTkButton(self, text="Number System Converter", command=lambda: App().mainloop()).pack(padx=10, pady=10)
        CTkButton(self, text="Temporary Files Cleaner".center(23), command=Temp_clean).pack(padx=10, pady=10)
        CTkButton(self, text="Organize Files".center(23), command=File_organizer).pack(padx=10, pady=10)


try:
    main().mainloop()
except:
    pass
