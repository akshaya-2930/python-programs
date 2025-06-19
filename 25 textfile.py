def write_to_file(filename):
    with open(filename, 'w') as f:
        text = input("Enter text to write to the file: ")
        f.write(text)
        print(f"Successfully written to '{filename}'.")

def read_from_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Contents of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")import file_operations

def main():
    filename = "sample.txt"
    file_operations.write_to_file(filename)
    file_operations.read_from_file(filename)

if __name__ == "__main__":
    main()
