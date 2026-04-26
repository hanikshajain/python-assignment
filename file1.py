# 1.1 Create and access list elements
my_list = [10, 20, 30, 40, 50]

print("Original List:", my_list)

# Access elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])


# 1.2 Add and Remove list elements

# Adding elements
my_list.append(60)          # Add at end
my_list.insert(2, 25)       # Add at specific position

print("\nList after adding elements:", my_list)

# Removing elements
my_list.remove(30)          # Remove specific value
popped = my_list.pop()      # Remove last element

print("List after removing elements:", my_list)
print("Popped element:", popped)


# 1.3 Sort list elements
my_list.sort()              # Ascending order
print("\nSorted List (Ascending):", my_list)

my_list.sort(reverse=True)  # Descending order
print("Sorted List (Descending):", my_list)


# 1.4 Reverse list elements
my_list.reverse()
print("\nReversed List:", my_list)