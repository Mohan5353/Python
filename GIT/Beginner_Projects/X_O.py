from numpy import array, full
from os import system
# from platform import system as sys
from time import sleep
from logging import warning, basicConfig, WARNING
from colorama import Fore, Style

basicConfig(level=WARNING, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S %p")


def clean():
    # if sys() == 'Windows':
    #     system('cls')
    # else:
    #     system('clear')
    system('cls')


def letter(i: int) -> None:
    my_arr = array([["   #   ", "  ##   ", "   #   ", "   #   ", "   #   ", "   #   ", " ##### "],
                    [" ##### ", "     # ", "     # ", " ##### ", " #     ", " #     ", " ##### "],
                    [" ##### ", "     # ", "     # ", " ##### ", "     # ", "     # ", " ##### "]])
    print('\n')
    for r in my_arr[i]:
        print(str(r).rjust(59))


def Instructions():
    print('\n\n')
    print("Make 3 Continuously in a Row".rjust(60))
    input("Press Enter to Continue...")


def start() -> None:
    Instructions()
    clean()
    for i in range(2, -1, -1):
        print("Game Starts in....\n")
        letter(i)
        sleep(1)
        clean()


arr = full((5, 5), ' ', dtype=str)
keys = array(["X", "O"], dtype=str)


# @lambda _: _()
def print_arr() -> None:
    global arr
    print('\n' * 3)
    for i in range(5):
        print(" " * 44, "|", end=" ")
        for j in range(5):
            print(arr[j][i], end=" | ")
        print('\n')
    print("1   2   3   4   5\n".rjust(65))


def Change(ID: int, row: int) -> int:
    global arr, keys
    i = 4
    while arr[row][i] != ' ':
        i -= 1
    arr[row][i] = keys[ID]
    return i


def Check(ID: int, row: int, i: int) -> int:
    global arr, keys
    count = 0
    while i < 5:
        if arr[row][i] == keys[ID]:
            count += 1
        else:
            break
        i += 1
    return count


def End() -> None:
    print(Style.BRIGHT + Fore.BLACK + ("\n" + " " * 50 + "Game Over"))


def End_Win(ID: int) -> None:
    global keys
    print(Style.BRIGHT + Fore.BLACK + ("\n" + " " * 50 + f"Player {keys[ID % 2]} Won"))


if __name__ == "__main__":
    start()
    print_arr()
    Id = 0
    end_chance = 0
    while True:
        try:
            inp = int(input(f"Player {keys[Id % 2]} Turn : ")) - 1
            clean()
            x = Change(Id % 2, inp)
            if x < 3:
                chance = Check(Id % 2, inp, x)
                if chance == 3:
                    End_Win(Id)
                    break
                elif x == 1 and chance == 1:
                    end_chance += 1
                # elif
                if end_chance == 5 or Id == 24:
                    End()
                    break
            Id += 1
        except Exception as e:
            if e == ValueError:
                warning("Invalid Input")
            else:
                warning("Row Is Full")
        finally:
            print_arr()
    sleep(15)
