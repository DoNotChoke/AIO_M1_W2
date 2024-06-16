def my_function(intergers, number=1):
    check = []
    for x in intergers:
        if x == number:
            check.append(True)
        else:
            check.append(False)
    return any(check)


my_list = [1, 3, 9, 4]
assert my_function(my_list, -1) == False
my_list = [1, 2, 3, 4]
print(my_function(my_list, 2))
