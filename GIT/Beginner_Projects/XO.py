from numpy import array, full
from os import system
# from platform import system as sys
from time import sleep
from colorama import Fore, Style


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


def start() -> None:
    clean()
    for i in range(2, -1, -1):
        print("Game Starts in....\n")
        letter(i)
        sleep(1)
        clean()


def instructions() -> None:
    print('\n\n')
    # print("Make 3 Continuously in a Row".rjust(60))
    input("Press Enter to Continue...")


def End() -> None:
    print(Style.BRIGHT + Fore.BLACK + ("\n" + " " * 50 + "Game Over"))


def End_Win(ID: int) -> None:
    print(Style.BRIGHT + Fore.BLACK + ("\n" + " " * 50 + f"Player {keys[ID % 2]} Won"))


arr = full((3, 3), ' ', dtype=str)
keys = array(["X", "O"], dtype=str)


# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def print_arr():
    print('\n' * 3)
    for i in range(3):
        print(" " * 44, "|", end=" ")
        for j in range(3):
            print(arr[i][j], end=" | ")
        print('\n')


if __name__ == "__main__":
    # start()
    instructions()
    print_arr()
