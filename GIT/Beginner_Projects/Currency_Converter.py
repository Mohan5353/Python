from requests import get
from json import dump, load
from datetime import datetime


def update():
    url = "https://v6.exchangerate-api.com/v6/a04cc39aea88ee70a55c180c/latest/USD"
    response = get(url).json()
    with open('Currency_Rate.json', 'w') as f:
        dump(response, f, indent=4)
    return response["conversion_rates"]


def get_response():
    with open('Currency_Rate.json') as f:
        return load(f)['conversion_rates']


def get_Quary():
    req: list[str, float, str] = [None, None, None]
    req[0] = input("Enter the Currency From: ").upper()
    req[1] = float(input("Value: "))
    req[2] = input("Enter the Currency To: ").upper()
    return req


if __name__ == '__main__':
    fun = input("Enter Method: ").lower()
    if fun == "-h":
        print("update - Update the Currency_Rate.json")
        print("get - Get the Currency_List")
        fun = input("Enter Method: ").lower()
    if fun == 'update':
        res = update()
    else:
        res = get_response()
        if fun == 'get':
            for c, i in enumerate(res.keys()):
                print(f'{i}: {res[i]}'.ljust(15), end='\t\t\t')
                if c % 4 == 3:
                    print()
            print('\n')
    info = get_Quary()
    ans = info[1] / res[info[0]] * res[info[2]]  # noqa
    print(f'{info[1]} {info[0]} = {ans} {info[2]} by {datetime.now():%H:%M:%S %p %d-%M-%Y}'.rjust(80))
    input("\nPress Enter to Continue...")
