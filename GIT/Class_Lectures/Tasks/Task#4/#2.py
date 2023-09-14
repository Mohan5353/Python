def Lst_2nd_Elem(Lst):
    if len(Lst) > 1:
        return Lst[1]
    else:
        return None


print(Lst_2nd_Elem([1, 2, 3]))
print(Lst_2nd_Elem([1]))
