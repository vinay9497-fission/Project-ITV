import sys

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <arg1> <arg2>")
        sys.exit(1)

    # Access arguments
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    # Print the arguments
    print(f"Argument 1: {arg1}")
    print(f"Argument 2: {arg2}")

if __name__ == "__main__":
    main()
