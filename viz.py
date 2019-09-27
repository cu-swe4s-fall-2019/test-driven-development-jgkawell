import get_data
import data_viz
import argparse

"""
This script enables the user to pipe in data through stdin and then
create plot files from it by choosing the file name and plot type.
"""

parser = argparse.ArgumentParser(
    description='Plot a data visualization from standard in (stdin).')
parser.add_argument(
    '--out_file',
    type=str,
    help='The file name of the plot to be generated')
parser.add_argument(
    '--plot_type',
    type=str,
    help='The type of plot to be generated (boxplot, histogram, or combo)')


def main():
    # Parse args and read in data from stdin
    args = parser.parse_args()
    data = get_data.read_stdin_col(col_num=0)

    try:
        # Switch case to choose the right plot type
        if args.plot_type == "boxplot":
            data_viz.boxplot(data, args.out_file)
        elif args.plot_type == "histogram":
            data_viz.histogram(data, args.out_file)
        elif args.plot_type == "combo":
            data_viz.combo(data, args.out_file)
        else:
            print("Only the following plot types are allowed: "
                  + "boxplot, histogram, or combo")
    except FileExistsError:
        print("That file already exists. "
              + "Either delete it or try another file name.")
        exit(1)


if __name__ == '__main__':
    main()
