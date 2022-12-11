########################################################################################
## PROBLEM 1 ##


# Implement the generate_models function.
#
# x and y are two lists corresponding to the x-coordinates and y-coordinates of the data samples (or data points);
# for example, if you have N data points, x = [x1 , x2 , ..., xN ] and y = [y1 , y2 , ..., yN ], where x_i and y_i are the x and y coordinate of the i-th data points.
# In this problem set, each x coordinate is an integer and corresponds to the year of a sample (e.g., 1997);
# each corresponding y coordinate is a float and represents the temperature observation (will be computed in multiple ways) of that year in Celsius.
# This representation will be used throughout the entire problem set.
# degs is a list of integers indicating the degree of each regression model that we want to create.
# For each model, this function should fit the data (x,y) to a polynomial curve of that degree.
# This function should return a list of models. A model is the numpy 1d array of the coefficients of the fitting polynomial curve.
# Each returned model should be in the same order as their corresponding integer in degs.
# Example:
#
# print(generate_models([1961, 1962, 1963],[4.4,5.5,6.6],[1, 2]))
# Should print something close to:
#
# [array([ 1.10000000e+00, -2.15270000e+03]), array([ -8.86320195e-14, 1.10000000e+00, -2.15270000e+03])]
# The above example was generating a linear and a quadratic curve on data samples (xi, yi ) = (1961, 4.4), (1962, 5.5), and (1963, 6.6).
# The resulting models are in the same order as specified in degs. Note that it is fine you did not get the exact number because of numerical errors.
#
# Note: If you want to use numpy arrays, you should add the following lines at the beginning of your code for the grader:
# import os
# os.environ["OPENBLAS_NUM_THREADS"] = "1"
# Then, do import numpy as np and use np.METHOD_NAME in your code. Unfortunately, pylab does not work with the grader.


import numpy as np
def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    Args:
        x: a list with length N, representing the x-coords of N sample points
        y: a list with length N, representing the y-coords of N sample points
        degs: a list of degrees of the fitting polynomial
    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    # TODO
    return [np.polyfit(x, y, z) for z in degs]


## Correct






########################################################################################
## PROBLEM 2 ##


# After we create some regression models, we also want to be able to evaluate our models to figure out how well each model represents our data,
# and tell good models from poorly fitting ones. One way to evaluate how well the model describes the data is computing the model's R^2 value.
# R^2 provides a measure of how well the total variation of samples is explained by the model.
#
# Implement the function r_squared. This function will take in:
#
# list, y, that represents the y-coordinates of the original data samples
# estimated, which is a corresponding list of y-coordinates estimated from the regression model
# This function should return the computed R^2 value. You can compute R^2 as follows,
# where  is the estimated y value for the i-th data point (i.e. predicted by the regression),  is the y value for the ith data point,
# and  is the mean of the original data samples.
#
# If you are still confused about R^2 , its wikipedia page has a good explanation about its use/how to calculate it.
#
# Note: If you want to use numpy arrays, you should add the following lines at the beginning of your code for the grader:
# import os
# os.environ["OPENBLAS_NUM_THREADS"] = "1"
# Then, do import numpy as np and use np.METHOD_NAME in your code. Unfortunately, pylab does not work with the grader.


import numpy as np

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    # TODO
    y, estimated = np.array(y), np.array(estimated)
    SEE = ((estimated - y)**2).sum()
    mMean = y.sum()/float(len(y))
    MV = ((mMean - y)**2).sum()
    return 1 - SEE/MV


## Correct


