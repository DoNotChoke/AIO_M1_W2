def my_function(x):
    ans = x[::-1]
    return ans


x = 'I can do it'
assert my_function(x) == 'ti od nac I'

x = 'apricot'
print(my_function(x))
