# 4.1 Create and access dictionary elements
student = {
    "name": "Vaibhavi",
    "age": 18,
    "course": "Engineering"
}

print("Original Dictionary:", student)

# Access elements
print("Name:", student["name"])
print("Age:", student.get("age"))


# 4.2 Update Dictionary

# Update existing value
student["age"] = 19

# Add new key-value pair
student["city"] = "Pune"

print("\nDictionary after update:", student)


# 4.3 Removing Elements

# Remove specific key
student.pop("course")

# Remove last inserted item
student.popitem()

print("Dictionary after removing elements:", student)


# 4.4 Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2   # Python 3.9+

print("\nMerged Dictionary:", merged_dict)