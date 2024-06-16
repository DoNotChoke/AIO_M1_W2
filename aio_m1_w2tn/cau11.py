def my_function(list_num=[0, 1, 2]):
    var = 0
    for i in list_num:
        var += i
    return var/len(list_num)


assert my_function([4, 6, 8]) == 6
print(my_function())
