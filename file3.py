# 3.1 Create and access tuple
tuple1 = (10, 20, 30, 40)

print("Tuple:", tuple1)

# Access elements
print("First element:", tuple1[0])
print("Last element:", tuple1[-1])


# 3.2 Nested Tuple
nested_tuple = (1, 2, (3, 4, 5), 6)

print("\nNested Tuple:", nested_tuple)
print("Access nested element:", nested_tuple[2][1])  # Access 4


# 3.3 Repetition of tuple
repeated_tuple = tuple1 * 2

print("\nRepeated Tuple:", repeated_tuple)


# 3.4 Concatenation of tuples
tuple2 = (50, 60)

concatenated_tuple = tuple1 + tuple2

print("\nConcatenated Tuple:", concatenated_tuple)