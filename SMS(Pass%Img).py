import pandas as pd
from PIL import Image
# import urllib.request as url
import time

data = pd.read_excel("StudentData.xlsx")
while True:
    Id = int(input("Enter Id or Quit :"))
    if Id == -1:
        break
    try:
        details = data.loc[Id]
        print(details)
        if input('Show Image?(Y/n) ').lower() == 'y':
            try:
                Image.open(r'C:/Users/bannu/Downloads/SMS_Pics/' + Id + r'.jpg').show()
            except Exception as e:
                print("\nFile Not Located...!", "\nException Raised:", e, end='\n\n')
        # if input('Open SMS?(Y/n) ').lower() == 'y':
        #     url.urlopen("https:// intranet.rguktn.ac.in/SMS/", Id, str(details["Password"]).split()[1])
    except Exception as e:
        print("\nFile Not Located...!", "\nException Raised:", e, end='\n\n')
time.sleep(2)
