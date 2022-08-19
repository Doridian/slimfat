from sys import argv

from makefat import make_fat


def main():
    make_fat(argv[1], argv[2:])


if __name__ == "__main__":
    main()
