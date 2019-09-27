import sys
import argparse

"""
This library/script contains allows the user
to read in an array from stdin giving a
specific column number.
"""

parser = argparse.ArgumentParser(
    description='Read in data from stdin by column number')
parser.add_argument(
    '--col_num',
    type=int,
    help='The column of stdin data to be read')


def read_stdin_col(col_num):
    """
    Pulls out the data from stdin for a given
    column and returns it as an int array.

    Parameters
    ----------
    col_num : the column number to read from stdin

    Returns
    ----------
    stdin_list : the array of ints from the column

    """

    # Iterate through the lines in stdin
    stdin_list = []
    for el in sys.stdin:
        try:
            # Split the line and read data into an int for col_num
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
    # Simply parse the arguments, call method, and print
    args = parser.parse_args()
    stdin_list = read_stdin_col(args.col_num)
    print(stdin_list)


if __name__ == "__main__":
    main()
