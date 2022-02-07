import sys
import re


PATTERN = "\-(.+)\:.+(hsl.+)"
TAB = "    "


def main():
    path = ""
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("Please provide a path to a file")
        return
    file = open(path, "r")
    print(":root {")
    lines = [line for line in file.read().splitlines() if line]
    for line in lines:
        if re.match(PATTERN, line):
            m = re.match(PATTERN, line)
            print(f"{TAB}--{camelCase(m.group(1))}: {m.group(2)};")
    print("}")


def camelCase(st):
    s = st.title()
    d = "".join(s.split())
    d = d.replace(d[0], d[0].lower())
    return d


if __name__ == "__main__":
    main()
