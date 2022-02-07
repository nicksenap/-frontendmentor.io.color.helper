import sys
import re


PATTERN = "\-(.+)\:.+(hsl.+)"
TAB = "    "


def main():
    path = ""
    mode = "sass"
    if len(sys.argv) > 2:
        mode = sys.argv[2]
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("Please provide a path to a file")
        return
    file = open(path, "r")
    if mode == "css":
        print(":root {")
    lines = [line for line in file.read().splitlines() if line]
    for line in lines:
        if re.match(PATTERN, line):
            m = re.match(PATTERN, line)
            if mode == "css":
                print(f"{TAB}--{camelCase(m.group(1))}: {m.group(2)};")
            elif mode == "sass":
                print(f"${kebabCase(m.group(1).strip().lower())}: {m.group(2)};")
    if mode == "css":
        print("}")


def camelCase(st):
    s = st.title()
    d = "".join(s.split())
    d = d.replace(d[0], d[0].lower())
    return d


def kebabCase(st):
    return st.replace(" ", "-")


if __name__ == "__main__":
    main()
