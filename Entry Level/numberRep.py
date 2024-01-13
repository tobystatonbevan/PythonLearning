my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
cleanList = []
for i in my_list:
    if i in cleanList:
        pass
    else:
        cleanList.append(i)
my_list = cleanList[:]
#
print("The list with unique elements only:")
print(my_list)
