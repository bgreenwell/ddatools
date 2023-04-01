from pandas import read_csv
from pkg_resources import resource_filename


def load_default():
    """Credit card default data

    Load the (simulated) credit card default data from James et. al. (2013).

    Parameters
    ----------
    None

    Returns
    -------
    DataFrame
        A Pandas data frame with 10000 observations on the following four 
        variables:

        * ``default`` - a binary variable with levels "No" and "Yes", indicating whether the customer defaulted on their debt;
        * ``student`` - a binary variable with levels "No" and "Yes", indicating whether the customer is a student;
        * ``balance`` - the average balance that the customer has remaining on their credit card after making their monthly payment;
        * ``income`` - income of customer.


    References
    ----------
    James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) An 
    Introduction to Statistical Learning with applications in R, 
    https://www.statlearning.com, Springer-Verlag, New York.
    """
    return read_csv(resource_filename("ddatools", "data/default.csv"))


def load_ticdata():
    """The Insurance company (TIC) benchmark

    Load the data mining benchmark data set use din the CoIL Challenge 2000; 
    for details about the competition, description of the columns, etc., see
    the associated competition's 
    `homepage <https://liacs.leidenuniv.nl/~puttenpwhvander/library/cc2000/>`_.

    Parameters
    ----------
    None

    Returns
    -------
    DataFrame
        A Pandas data frame with 9822 observations on 86 variables; for a 
        description of each column, see the associated
        `data description page <https://liacs.leidenuniv.nl/~puttenpwhvander/library/cc2000/data.html>`_.

    Notes
    -----
    The first 5822 rows correspond to the original training data, leaving the rest for validation.

    References
    ----------
    Peter van der Putten, Michel de Ruiter, Maarten van Someren CoIL Challenge 2000 Tasks and Results: 
    Predicting and Explaining Caravan Policy Ownership http://www.liacs.nl/~putten/library/cc2000/.
    """
    return read_csv(resource_filename("ddatools", "data/ticdata.csv"))


def load_bank():
    """Bank marketing data set (UCI)"""
    return read_csv(resource_filename("ddatools", "data/bank.csv"))


def load_credit():
    """Default of credit card clients (UCI)"""
    return read_csv(resource_filename("ddatools", "data/credit.csv"))
