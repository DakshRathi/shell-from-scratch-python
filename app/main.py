import sys


def handle_exit(args):
    """Handle the exit builtin command."""
    if len(args) > 0:
        exit_code = int(args[0])
        sys.exit(exit_code)
    else:
        sys.exit(0)


def handle_echo(args):
    """Handle the echo builtin command."""
    if args:
        # Join arguments with spaces and print
        output = " ".join(args)
        print(output)
    else:
        # Echo with no arguments prints empty line
        print()


def handle_type(args, builtin_commands):
    """Handle the type builtin command."""
    if not args:
        print("type: missing argument", file=sys.stderr)
        return
    
    for command_name in args:
        if command_name in builtin_commands:
            print(f"{command_name} is a shell builtin")
        else:
            print(f"{command_name}: not found")


def main():
    builtin_commands = {"echo", "exit", "type"}

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
            handle_exit(args)
        elif command == "echo":
            handle_echo(args)
        elif command == "type":
            handle_type(args, builtin_commands)
        else:
            print(f"{command_line}: command not found")


if __name__ == "__main__":
    main()
