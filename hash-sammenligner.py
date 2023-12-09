import os
import hashlib

def calculate_hash(file_path, algorithm="sha256"):
    """
    Calculate the hash value of a file using the specified algorithm.

    Parameters:
    - file_path (str): The path to the file.
    - algorithm (str): The hash algorithm (default is "sha256").

    Returns:
    - str: The hash value.
    """
    hasher = hashlib.new(algorithm)
    with open(file_path, "rb") as file:
        # Read the file in chunks to handle large files
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def verify_hash(file_path, stored_hash_file):
    """
    Verify the hash of a file against a stored hash value.

    Parameters:
    - file_path (str): The path to the file to be verified.
    - stored_hash_file (str): The path to the file containing the stored hash.

    Returns:
    - bool: True if the hashes match, False otherwise.
    """
    try:
        with open(stored_hash_file, "r") as stored_hash_file:
            stored_hash = stored_hash_file.read().strip()
    except FileNotFoundError:
        print("Stored hash file not found.")
        return False

    calculated_hash = calculate_hash(file_path)

    if stored_hash == calculated_hash:
        print("Hashes match. File is verified.")
        return True
    else:
        print("Hashes do not match. File verification failed.")
        return False

def list_files_in_folder():
    current_folder = os.getcwd()
    files_in_folder = [f for f in os.listdir(current_folder) if os.path.isfile(os.path.join(current_folder, f))]
    return files_in_folder

def main():
    # List files in the current folder
    files_in_folder = list_files_in_folder()
    print("Files in the current folder:")
    for i, file in enumerate(files_in_folder, start=1):
        print(f"{i}. {file}")

    # User chooses the file
    file_index = input("Enter the number corresponding to the file you want to verify: ")

    try:
        selected_file = files_in_folder[int(file_index) - 1]
        file_path = os.path.join(os.getcwd(), selected_file)

        # List hash files in the current folder
        hash_files_in_folder = [f for f in os.listdir(os.getcwd()) if f.endswith(".txt")]
        print("\nHash files in the current folder:")
        for i, hash_file in enumerate(hash_files_in_folder, start=1):
            print(f"{i}. {hash_file}")

        # User chooses the hash file
        hash_file_index = input("Enter the number corresponding to the hash file: ")

        try:
            selected_hash_file = hash_files_in_folder[int(hash_file_index) - 1]
            stored_hash_file = os.path.join(os.getcwd(), selected_hash_file)

            if verify_hash(file_path, stored_hash_file):
                print("File verification successful.")
            else:
                print("File verification failed.")
        except (ValueError, IndexError):
            print("Invalid selection for the hash file. Please enter a valid number.")
    except (ValueError, IndexError):
        print("Invalid selection for the file. Please enter a valid number.")

if __name__ == "__main__":
    main()
