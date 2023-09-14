from numpy import array, random
from time import sleep, time
# from platform import system as sys
from colorama import Fore, Style
from os import system


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


class Random:
    def __int__(self):
        self.num = random.randint(1, 11, 1)


if __name__ == '__main__':
    # start()
    t1: float() = time()
    count: int = 0
    print(t1)
