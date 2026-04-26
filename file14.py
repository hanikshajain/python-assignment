try:
    filename = input("Enter the filename: ")

    # Try opening the file in read mode
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)

# Exception: File not found
except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename.")

# Exception: Permission denied
except PermissionError:
    print("Error: You do not have permission to read this file.")

# Optional: any other unexpected error
except Exception as e:
    print("An unexpected error occurred:", e)