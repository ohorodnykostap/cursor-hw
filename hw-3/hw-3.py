# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))
            # 9790720
            # 140000319756400
            # 140000319727424
            # 140000320634560
            # 140000320561024

# 2. Append 4 and 5 to the lst_d and define the id one more time.

lst_d.append(4)
lst_d.append(5)
print(id(lst_d))
            # 140446229827264

# 3. Define the type of each object from step 1.

print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))
            # <class 'int'>
            # <class 'str'>
            # <class 'set'>
            # <class 'list'>
            # <class 'dict'>

# 4. Check the type of the objects by using isinstance.

print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))
            # True
            # True
            # True
            # True
            # True

# 5. With .format and curly braces {}

print("Anna has {} apples and {} peaches.".format(5, 5))
            # Anna has 5 apples and 5 peaches.

# 6. By passing index numbers into the curly braces.

print("Anna has {0} apples and {1} peaches.".format(5, 5))
            # Anna has 5 apples and 5 peaches.

# 7. By using keyword arguments into the curly braces.
print("Anna has {0} apples and {1} peaches.".format('one', 'two'))
            # Anna has 5 apples and 5 peaches.

# 8*. With indicators of field size (5 chars for the first and 3 for the second)

print("Anna has {0:5} apples and {1:3} peaches.".format('one', "two"))
            # Anna has one   apples and two peaches.

# 9. With f-strings and variables

a = 2
b = 3
print(f"Anna has {a} apples and {b} peaches.")
            # Anna has 2 apples and 3 peaches.

# 10. With % operator

app = 2
peach = 3
print("Anna has %a apples and %a peaches." % (app, peach))
            # Anna has 2 apples and 3 peaches.

# 11*. With variable substitutions by name (hint: by using dict)

apple = 3
peach = 3
data_dict = {"apl": apple, "peach": peach}
print("Anna has %(apl)d apples and %(peach)d peaches." % data_dict)
            # Anna has 3 apples and 3 peaches.

# 12. Convert (1) to list comprehension

list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)
            #[0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

# 13. Convert (2) to regular for with if-else

lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)
            #[0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

#14 Convert (3) to dict comprehension.

dict_comprehension = {d: d ** 2 for d in range(1, 11) if d % 2 == 1}
print(dict_comprehension)
            # {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 15*. Convert (4) to dict comprehension.

dict_comprehension = {d: d ** 2 if d % 2 == 1 else d // 0.5 for d in range (1, 11)}
print(dict_comprehension)
            # {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

#16. Convert (5) to regular for with if.

x = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        x[num] = num ** 3
print(x)
            #{0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

# 17*. Convert (6) to regular for with if-else.

d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
    else:
        d[x] = x
print(d)
            # {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}

# 18. Convert (7) to lambda function

foo = lambda x, y: x if x < y else y
print(foo(4, 3))
            # 3

# 19*. Convert (8) to regular function

def foo(x, y, z):
    if x < y and x > z:
        return z
    else:
        return y

print(foo(1, 2, 3))
            # 2

# 20. Sort lst_to_sort from min to max

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
            # [1, 5, 13, 15, 18, 24, 33, 55]

# 21. Sort lst_to_sort from max to min

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort, reverse=True))
            # [55, 33, 24, 18, 15, 13, 5, 1]

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
new_lst_to_sort = list(map(lambda x: x * 2, lst_to_sort))
print(new_lst_to_sort)
            # [10, 36, 2, 48, 66, 30, 26, 110]

# 23*. Raise each list number to the corresponding number on another list:

list_A = [2, 3, 4]
list_B = [5, 6, 7]
up_number = list(map(lambda x, y: x+y, list_A, list_B))
print(up_number)
            # [7, 9, 11]

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.

from  functools import reduce
foo = reduce(lambda x,y: x+y, lst_to_sort)
print(foo)
            # 164

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
new_list = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(new_list)
            # [5, 1, 33, 15, 13, 55]

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

lst_neg = list(filter(lambda x: x < 0, range(-10, 10)))
print(lst_neg)

            # [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 27*. Using the filter function, find the values that are common to the two lists:

list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
list_3 = list(filter(lambda x: x in list_1, list_2))
print(list_3)
            # [2, 3, 5, 7]