import sys


def main():
    sys.stdout.write("$ ")
    command = input()
    while command != "exit":
        print(f"{command}: command not found")
        sys.stdout.write("$ ")
        command = input()


if __name__ == "__main__":
    main()
