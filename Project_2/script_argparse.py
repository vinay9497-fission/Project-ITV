import argparse

def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument('arg1', type=str, help='The first argument')
    parser.add_argument('arg2', type=str, help='The second argument')
    args = parser.parse_args()

    print(f"Argument 1: {args.arg1}")
    print(f"Argument 2: {args.arg2}")

if __name__ == "__main__":
    main()