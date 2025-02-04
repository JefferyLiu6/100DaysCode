list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(i) for i in list_of_strings]
result = [i for i in numbers if i%2 == 0]
print(result)