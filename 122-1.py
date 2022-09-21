# 122-1.py
import sys


def main():
    # sys.stdin will read whatever in <
    contents = sys.stdin.read()
    new_content = contents.replace(sys.argv[1], sys.argv[2])
    sys.stdout.write(new_content)


main()
