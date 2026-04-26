# 2.1 Create and access set elements
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Set 1:", set1)
print("Set 2:", set2)

# Accessing elements (using loop since sets are unordered)
print("\nElements of Set 1:")
for item in set1:
    print(item)


# 2.2 Union of elements
union_set = set1.union(set2)
print("\nUnion of Set 1 and Set 2:", union_set)


# 2.3 Intersection of elements
intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)


# 2.4 Difference of elements
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)

print("Difference (Set1 - Set2):", difference_set1)
print("Difference (Set2 - Set1):", difference_set2)