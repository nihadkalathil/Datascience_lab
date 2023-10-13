days_list = []
days_tuple = ()
days_dict = {}
days_set = set()
for i in range(7):
    day = input(f"Enter day {i + 1}: ")
    days_list.append(day)
    days_tuple += (day,)
    days_dict[i + 1] = day
    days_set.add(day)
print("\nList:")
print(days_list)
print(f"Type: {type(days_list)}")
print("\nTuple:")
print(days_tuple)
print(f"Type: {type(days_tuple)}")
print("\nDictionary:")
print(days_dict)
print(f"Type: {type(days_dict)}")
print("\nSet:")
print(days_set)
print(f"Type: {type(days_set)}")