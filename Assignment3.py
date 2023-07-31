import shutil

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File Contents:")
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied while trying to read '{filename}'.")
    except IOError as e:
        print(f"Error: Unable to read '{filename}'. {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading '{filename}'. {e}")

def append_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content + "\n")
            print(f"Successfully appended '{content}' to '{filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied while trying to append '{filename}'.")
    except IOError as e:
        print(f"Error: Unable to append to '{filename}'. {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred while appending to '{filename}'. {e}")

def copy_file(source, destination):
    try:
        shutil.copyfile(source, destination)
        print(f"Successfully copied '{source}' to '{destination}'.")
    except FileNotFoundError:
        print(f"Error: The file '{source}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied while trying to copy '{source}' to '{destination}'.")
    except IOError as e:
        print(f"Error: Unable to copy '{source}' to '{destination}'. {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred while copying '{source}' to '{destination}'. {e}")

def delete_file(filename):
    try:
        # Use the remove function from the os module to delete the file
        os.remove(filename)
        print(f"Successfully deleted '{filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied while trying to delete '{filename}'.")
    except IOError as e:
        print(f"Error: Unable to delete '{filename}'. {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred while deleting '{filename}'. {e}")

def handle_exception(func, *args):
    try:
        func(*args)
    except Exception as e:
        print(f"Error: An unexpected error occurred. {e}")

def main():
    # The filename for our text file
    filename = "data.txt"

    # Task 1: Read and print the contents of the file
    print("--- Task 1: Read File ---")
    handle_exception(read_file, filename)

    # Task 2: Append a user-provided string to the file
    print("\n--- Task 2: Append to File ---")
    content_to_append = input("Enter the content to append: ")
    handle_exception(append_file, filename, content_to_append)

    # Task 3: Copy the file to a new file called "data_copy.txt"
    print("\n--- Task 3: Copy File ---")
    handle_exception(copy_file, filename, "data_copy.txt")

    # Task 4: Delete the file
    print("\n--- Task 4: Delete File ---")
    handle_exception(delete_file, filename)

if __name__ == "__main__":
    main()