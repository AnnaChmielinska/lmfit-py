# -*- coding: utf-8 -*-

"""Provide the Statistic object.

Statistic provides definition of objective function and optimization method
for fitting process.

"""

from abc import ABCMeta, abstractmethod

class Statistic():
    """Abstract class for the Statistic object.

    Parameters
    ----------
    name : str
    optimization_method : str
        One of: 'nelder', 'powell', 'leastsq'.

    Methods
    -------
    objective_func : ndarray

    """

    __metaclass__ = ABCMeta

    def __init__(self, name, optimization_method):
        """Initialize a Statistic object.

        Parameters
        ----------
        name : str
        optimization_method : str
            One of: 'nelder', 'powell', 'leastsq'.

        """
        self.name = name
        self.optimization_method = optimization_method

    @abstractmethod
    def objective_func(self, *args, **kwargs):
        """Objective function for optimization."""
        raise NotImplementedError("`Statistic.objective_func` not implemented")