

import os

def read_and_modify_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (example: add a prefix)
        modified_content = "Modified: " + content

        # Write the modified content to a new file
        with open('modified_' + filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"File '{filename}' modified successfully. New file: 'modified_{filename}'")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except IOError:
        print(f"Error reading or writing file '{filename}'.")

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    read_and_modify_file(filename)
