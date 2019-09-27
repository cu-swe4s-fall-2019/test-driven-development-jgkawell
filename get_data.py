import sys
import argparse


parser = argparse.ArgumentParser(
    description='Read in data from stdin by column number')
parser.add_argument(
    '--col_num',
    type=int,
    help='The column of stdin data to be read')


def read_stdin_col(col_num):
    stdin_list = []
    for el in sys.stdin:
        try:
            stdin_list.append(int(el.split()[col_num]))
        except ValueError:
            print("Input from stdin must only contain integer values")
            sys.exit(1)
        except IndexError:
            print("The 'col_num' was either too big or too small "
                  + "for the data given.\n"
                  + "This could be because no data was in stdin.")
            sys.exit(1)

    return stdin_list


def main():
    args = parser.parse_args()
    stdin_list = read_stdin_col(args.col_num)
    print(stdin_list)


if __name__ == "__main__":
    main()
