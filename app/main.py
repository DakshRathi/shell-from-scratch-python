import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command_line = input()
        parts = command_line.split()

        if not parts:
            continue

        command = parts[0]

        if command == "exit":
            if len(parts) > 1:
                exit_code = int(parts[1])
                sys.exit(exit_code)
            else:
                sys.exit(0)
        else:
            print(f"{command_line}: command not found")


if __name__ == "__main__":
    main()
