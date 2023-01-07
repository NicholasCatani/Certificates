import numpy as np
import pandas as pd
from typing import List, Tuple
import copy
import statsmodels.api as sm
import matplotlib.pyplot as plt

##############################################################################################

def infinite_sequence():
    num = 1
    while True:
        yield str(num)
        num += 1


name_sequence = infinite_sequence()


def next_name():
    return next(name_sequence)


def reset_names():
    global name_sequence
    name_sequence = infinite_sequence()


class Company:

    def __init__(self, i: float, s: float, name: str = None):
        self._i = float(i)
        self._s = float(s)
        self._name = name
        self._production = None
        self._regression_data = None

        if not name:
            self._name = next_name()

    @property
    def i(self):
        """
        The intercept of the estimated marginal cost curve
        Type: float
        """
        return self._i

    @property
    def s(self):
        """
        The slope of the estimated marginal cost curve
        Type: float
        """
        return self._s

    @property
    def equation(self) -> str:             # Here to set up firm's total cost function
        """
        The slope of the estimated marginal cost curve
        Type: float
        """
        return f"Mc = {str(round(self._i))} + {str(round(self._s))} * q"

    @property
    def full_equation(self) -> str:
        """
        The slope of the estimated marginal cost curve
        Type: float
        """
        return f"Mc = {str(self._i)} + {str(self._s)} * q"

    @property
    def name(self):
        """
        A name to identify the company
        Type: string
        """
        return self._name

    @property
    def production(self):
        """
        A name to identify the company
        Type: float
        """
        return self._production

    @property
    def regression_data(self):
        """
        Regression data from OLS regression.
        """
        return self._regression_data

    def set_prod(self, production: float):
        """
        Set the production of the company in the current market
        """
        self._production = production
        return self

    def set_name(self, name: str):
        """
        Set a name to identify the company by
        """
        self._name = name
        return self

    def profits(self, p: float):
        """
        The profits of the company
        Type: float
        """
        return (p * self._production) - (self._i +
                                         self._s * self._production
                                         ) * self._production

    def set_regression_data(self, stuff):
        self._regression_data = stuff
        return self


Demand = Tuple[float, float]
CompanyList = List[Company]


def calculate_price(total_q: float, demand: Demand) -> float:
    """
    Calculates the equilibrium price, given a linear Demand curve and
    the total units produced by the companies
    Args:
      total_q: The total units produced
      demand: The parameters of a linear demand curve
    Returns:
      The equilibrium price
    """
    return demand[0] - demand[1] * total_q


def set_cournot_production(demand: Demand,
                           companies: CompanyList) -> CompanyList:
    """
    Return a list with the addition of the production units in
    every company in the given list, when all companies are in a
    Cournot competition.
    Args:
        demand: Market's demand
        companies: A list of companies
    Returns: Company_List with updated production values
    """
    # Create an array of length N -> (M_i + 2 * B)
    diagonal: List[float] = [x.s + 2 * demand[1] for x in companies]

    dimension = len(companies)

    # Create a matrix of N x N dimension filled with B
    x = np.full((dimension, dimension), demand[1], dtype=float)

    # Replace the diagonal of the matrix with (M_i + 2 * B)
    # This creates matrix named H in the documentation above
    # noinspection PyTypeChecker
    np.fill_diagonal(x, diagonal)

    # Create a matrix N x 1 with ( A - K ) -- Named U in the documentation above
    constants = [demand[0] - comp.i for comp in companies]

    # Our solution is an array of quantities, length N.
    productions = np.linalg.solve(x, constants).flatten()

    for i, c in enumerate(companies):
        c.set_prod(productions[i])

    return companies

######################################################################################

def market_stats_dump(companies: CompanyList, q: int, p: int):
    """
    Print data for the market.
    """
    a, b = D[0], D[1]
    print(
        f"The demand curve is: Q = {round(abs(a / b))} - {round(1 / abs(b))} * P\n",
        f"\t Whereas, the inverse: P = {round(a)} - {round(b)} * Q\n")

    for comp in companies:
        print(f"- Firm {comp.name} with {comp.equation}\n"
              f"\tproduces {round(comp.production)} outputs",
              f" with ${round(comp.profits(p))} in profit.\n")

    print(f"Total production is {round(q)} with market price of ${round(p)}.")

####################################################################################### Testing

D = (100, 1)    # Inverse demand curve =>  P = K - cQ
companies: CompanyList = [Company(20, 0),
                          Company(30, 0)]

companies = set_cournot_production(D, companies)
quantity = sum([comp.production for comp in companies])
price = calculate_price(quantity, D)

market_stats_dump(companies, quantity, price)                   # Profit check => [(P - Mc) * qi] / 2 #

############# Debug completed! Algorithm runs effectively.