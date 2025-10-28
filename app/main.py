import sys


def main():
    sys.stdout.write("$ ")
    while True:
        # Wait for user input
        command = input()
        print(f"{command}: command not found")
        sys.stdout.write("$ ")


if __name__ == "__main__":
    main()
