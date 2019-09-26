import os
import math_lib as ml
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('Agg')


def boxplot(L, out_file_name):

    if os.path.exists(out_file_name):
        raise FileExistsError("That file name already exists.")

    mean = ml.list_mean(L)
    stdev = ml.list_stdev(L)
    plt.boxplot(L)
    plt.title("mean: " + str(mean) + " stdev: " + str(stdev))
    plt.xlabel("Column Number")
    plt.ylabel("Value")
    plt.savefig(out_file_name, bbox_inches="tight")
    plt.close()


def histogram(L, out_file_name):

    if os.path.exists(out_file_name):
        raise FileExistsError("That file name already exists.")

    mean = ml.list_mean(L)
    stdev = ml.list_stdev(L)
    plt.hist(L)
    plt.title("mean: " + str(mean) + " stdev: " + str(stdev))
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig(out_file_name, bbox_inches="tight")
    plt.close()


def combo(L, out_file_name):

    if os.path.exists(out_file_name):
        raise FileExistsError("That file name already exists.")

    mean = ml.list_mean(L)
    stdev = ml.list_stdev(L)
    plt.title("mean: " + str(mean) + " stdev: " + str(stdev))

    plt.subplot(1, 2, 1)
    plt.boxplot(L)
    plt.xlabel("Column Number")
    plt.ylabel("Value")

    plt.subplot(1, 2, 2)
    plt.hist(L)
    plt.xlabel("Value")
    plt.ylabel("Frequency")

    plt.savefig(out_file_name)
    plt.close()
