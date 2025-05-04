def test(tuple):
    result = []
    for item in tuple:
       result.append (item)
    return result
my_tuple = ("Nziza", "Tayali", 18, 162, 58, "Math")
print("\nOriginal tuple: ")
print(my_tuple)
print("\nConverted tuple to list: ")
print(test(my_tuple))