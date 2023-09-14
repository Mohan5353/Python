print("Safety Prediction".center(50, "-"))
print("Instructions:")
print("\tAnswer The Following Questions in Yes or No format\n")
try:
    if input("Is Today a Working Day? ").lower() == "yes":
        if input("Is it Raining too Heavy? ").lower() == "yes":
            if input("Do You have an Umbrella? ").lower() == "yes":
                print("_You are Safe_".center(50, "*"))
            else:
                print("_You are Not Safe_".center(50, "x"))
        else:
            if input("Do You have a Hoody? ").lower() == "yes":
                print("_You are Safe_".center(50, "*"))
            else:
                print("_You are Not Safe_".center(50, "x"))
    else:
        print("_You are Safe_".center(50, "*"))
except:
    print("Plz Answer in Yes or No format".center(50, "x"))
finally:
    print("Thank You".center(50, "-"))
