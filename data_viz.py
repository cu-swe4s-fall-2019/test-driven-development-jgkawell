import os
import math_lib as ml
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('Agg')

"""
This library contains a few plot functions
for lists of numeric values. Enables the saving
of plot files for boxplot, histogram, and combo
of the two.
"""


def boxplot(array, out_file_name):
    """
    Creates and saves a boxplot of the data given
    in a 1D numeric list. Mean and standard deviation
    are found and shown in the title.

    Parameters
    ----------
    array : list of ints or doubles
    out_file_name : string name of file to save

    Returns
    ----------

    """

    # Make sure not to overwrite an existing file
    if os.path.exists(out_file_name):
        raise FileExistsError("That file name already exists.")

    # Find mean and stdev using math_lib library
    mean = ml.list_mean(array)
    stdev = ml.list_stdev(array)

    # Create and save the plot
    plt.boxplot(array)
    plt.title("mean: " + str(mean) + " stdev: " + str(stdev))
    plt.xlabel("Column Number")
    plt.ylabel("Value")
    plt.savefig(out_file_name, bbox_inches="tight")
    plt.close()


def histogram(array, out_file_name):
    """
    Creates and saves a histogram of the data given
    in a 1D numeric list. Mean and standard deviation
    are found and shown in the title.

    Parameters
    ----------
    array : list of ints or doubles
    out_file_name : string name of file to save

    Returns
    ----------

    """

    # Make sure not to overwrite an existing file
    if os.path.exists(out_file_name):
        raise FileExistsError("That file name already exists.")

    # Find mean and stdev using math_lib library
    mean = ml.list_mean(array)
    stdev = ml.list_stdev(array)

    # Create and save the plot
    plt.hist(array)
    plt.title("mean: " + str(mean) + " stdev: " + str(stdev))
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig(out_file_name, bbox_inches="tight")
    plt.close()


def combo(array, out_file_name):
    """
    Creates and saves a combo plot of the data given
    in a 1D numeric list. Mean and standard deviation
    are found and shown in the title. The combo consists
    of a boxplot and histogram side-by-side.

    Parameters
    ----------
    array : list of ints or doubles
    out_file_name : string name of file to save

    Returns
    ----------

    """

    # Make sure not to overwrite an existing file
    if os.path.exists(out_file_name):
        raise FileExistsError("That file name already exists.")

    # Find mean and stdev using math_lib library
    mean = ml.list_mean(array)
    stdev = ml.list_stdev(array)

    # Set the global title
    plt.title("mean: " + str(mean) + " stdev: " + str(stdev))

    # Create the boxplot on the left
    plt.subplot(1, 2, 1)
    plt.boxplot(array)
    plt.xlabel("Column Number")
    plt.ylabel("Value")

    # Create the histogram on the right
    plt.subplot(1, 2, 2)
    plt.hist(array)
    plt.xlabel("Value")
    plt.ylabel("Frequency")

    # Save and close the plots
    plt.savefig(out_file_name)
    plt.close()
