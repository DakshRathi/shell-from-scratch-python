import sys
import shutil


def exit_cmd(args):
    if len(args) > 1:
        sys.exit(int(args[1]))
    sys.exit(0)


def echo_cmd(args):
    if len(args) > 1:
        print(" ".join(args[1:]))
    else:
        print()


def type_cmd(args):
    if len(args) < 2:
        print("type: missing argument", file=sys.stderr)
        return
    
    for command_name in args[1:]:
        if command_name in BUILT_INS:
            print(f"{command_name} is a shell builtin")
        elif full_path := shutil.which(command_name):
            print(f"{command_name} is {full_path}")
        else:
            print(f"{command_name}: not found")


BUILT_INS = {
    'exit': exit_cmd,
    'echo': echo_cmd,
    'type': type_cmd
}


def main():
    while True:
        sys.stdout.write("$ ")
        command = input().strip()
        
        if not command:
            continue

        parts = command.split()
        cmd = parts[0]

        if cmd in BUILT_INS:
            BUILT_INS[cmd](parts)
        else:
            print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
