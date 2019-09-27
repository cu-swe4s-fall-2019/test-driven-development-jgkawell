# test-driven-dev
Test Driven Development

## Description
This repository contains Python code for simple data analysis and visualization. It contains some basic libraries and a user facing script that takes in input from `stdin` and saves data plots to a file.

The math library gives you functions for finding the mean and standard deviation of a given 1D numeric list and the data visualization library gives you functions for saving boxplots, histograms, or combo plots for any 1D array of numeric data.

## How to use
The best way to use this project is simply to access the user-facing script `viz.py`. This script needs to be called by piping `stdin` through the command line. An example of this is given with the script `get_data.sh` with the below command:

```
bash gen_data.sh | python viz.py --out_file {your_file_name} --plot_type {your_plot_type}
```

If you want to know more about the options for `viz.py` simply run the command:

```
python viz.py -h
```

The two libraries provided (`math_lib` and `data_viz`) can be imported just like any other Python library. If you wish to run unit tests for these libraries you can run them with the following commands:

```
python test_math_lib.py
python test_data_viz.py
```

## Installation
The project only requires cloning the repository and making sure that you have Python 3 installed with `matplotlib`. Assuming Python 3 is already installed, you can run the below command to install the required package:

```
pip install matplotlib
```
