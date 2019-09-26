import sys


def read_stdin_col(col_num):
    stdin_list = []
    for el in sys.stdin:
        stdin_list.append(int(el.split()[col_num]))

    return stdin_list


def main():
    stdin_list = read_stdin_col(0)
    print(stdin_list)


if __name__ == "__main__":
    main()
