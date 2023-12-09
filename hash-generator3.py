import os
import hashlib




def calculate_hash(file_path, algorithm="sha256"):
    """
    Kalkulerer hashen basert på sha256 algoritmen
    
    - file_path (str): bruk som variable i fil-seleksjonen
    - algorithm (str): hash algoritmen (default = "sha256").

    Returnerer:
    - str: hash-verdien
    """
    hasher = hashlib.new(algorithm)
    with open(file_path, "rb") as file:

        # Les filen i 4096 chunks, for å håndtere større filer
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def save_hash_to_file(file_path, hash_value, output_file="placeholder"):
    """
    Lagrer hash-verdien til en fil

    Parameters:
    - file_path (str): hvor filen skal lagres
    - hash_value (str): hash-verdien
    - output_file (str): navnet på output filen som inneholder hashen (default is "placeholder").
    """
        # Get the filename without the extension
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))

    # Create the output filename with the chosen file's name, custom hash value, and extension
    output_file = f"{file_name}.hash.txt"

    with open(output_file, "w") as output:
        #"W" for write - overskriver hvis den kjøres på nytt
        output.write(hash_value)

def main():
    current_folder = os.getcwd()
    files_in_folder = [f for f in os.listdir(current_folder) if os.path.isfile(os.path.join(current_folder, f))]

    print("Files in the current folder:")
    for i, file in enumerate(files_in_folder, start=1):
        print(f"{i}. {file}")

    file_index = input("Enter the number corresponding to the file you want to hash: ")

    try:
        selected_file = files_in_folder[int(file_index) - 1]
        file_path = os.path.join(current_folder, selected_file)

        hash_value = calculate_hash(file_path)
        print(f"Hash value for {selected_file}: {hash_value}")

        save_hash_to_file(file_path, hash_value, selected_file)
        print(f"Hash value saved to {selected_file}")
    except (ValueError, IndexError):
        print("Invalid selection. Please enter a valid file number.")

if __name__ == "__main__":
    main()
