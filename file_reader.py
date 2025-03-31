def read_file(filename="sample.txt"):
    """
    Read and display contents of a file with error handling
    Args:
        filename (str): Name of file to read
    """
    try:
        with open(filename, 'r') as file:
            print(f"Contents of '{filename}':\n{'-'*30}")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    read_file()