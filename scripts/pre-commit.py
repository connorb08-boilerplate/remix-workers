import os
import subprocess


PRE_COMMIT_COMMANDS = ["yarn typecheck", "yarn lint", "yarn pretty"]
VERBOSE = True


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def main():
    # Add colors here
    print(
        f"{bcolors.HEADER + bcolors.UNDERLINE}Running pre-commit checks...{bcolors.ENDC}\n"
    )
    for command in PRE_COMMIT_COMMANDS:
        print(f"\t{bcolors.OKCYAN}Running {command}{bcolors.ENDC}")
        if VERBOSE:
            with subprocess.Popen(
                command.split(" "),
                stdout=subprocess.PIPE,
                bufsize=1,
                universal_newlines=True,
            ) as p:
                for line in p.stdout:
                    print(f"\t\t{line}", end="")  # process line here
                return_code = p.poll()
                if return_code:
                    print(f"\t{bcolors.FAIL}✗{bcolors.ENDC} {command}\n")
                    exit(1)
                else:
                    print(f"\t{bcolors.OKGREEN}✓{bcolors.ENDC} {command}\n")

        else:
            out = subprocess.run(command.split(" "), check=True, stdout=subprocess.PIPE)
            out = out.stdout.decode("utf-8")
            print(f"\t{bcolors.OKGREEN}✓{bcolors.ENDC} {command}\n")

    print(f"{bcolors.OKGREEN + bcolors.BOLD}All checks passed!{bcolors.ENDC}")


if __name__ == "__main__":
    main()
