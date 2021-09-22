import sys

def converter(s):
    s = "-".join(s).lower()
    s = "".join(filter(lambda i: i.isdigit() or i.isalpha() or i in ['-'], s))
    return s

if __name__ == "__main__":
    s = sys.argv[1:]
    print(converter(s))