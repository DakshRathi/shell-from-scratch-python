import sys

def handle_echo(args):
    """Handle the echo builtin command."""
    if args:
        # Join arguments with spaces and print
        output = " ".join(args)
        print(output)
    else:
        # Echo with no arguments prints empty line
        print()


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command_line = input()
        parts = command_line.split()

        if not parts:
            continue

        command = parts[0]
        args = parts[1:]

        if command == "exit":
            if len(parts) > 1:
                exit_code = int(parts[1])
                sys.exit(exit_code)
            else:
                sys.exit(0)
        elif command == "echo":
            handle_echo(args)
        else:
            print(f"{command_line}: command not found")


if __name__ == "__main__":
    main()
