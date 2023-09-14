from os import system as sys


class Temp_clean:
    def __init__(self):
        try:
            sys(r'del /q /f /s %temp%\\*')
            sys(r'del /s /q C:\\Windows\\temp\*')
        except Exception as e:
            print(e)
            input("Press Enter to Retry....")
        finally:
            print('Done...')

# Temp_clean()
