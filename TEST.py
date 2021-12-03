dict1 = {1: 1, 2: 9, 3: 4}
#sorted_values = sorted(dict1.values()) # Sort the values
#print(sorted_values)
#print()
print(*dict1.values())
sorted_keys = sorted(dict1, key=dict1.get)
print(sorted_keys)
