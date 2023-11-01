from abc import ABC, abstractmethod
import pandas as pd


class Operation(ABC):

    @abstractmethod
    def process(self, data: pd.Series) -> pd.Series:
        """
        Process the timeseries data and return the modified series.
        This method must be overridden by all subclasses.

        :param data: A pandas Series representing the timeseries.
        :return: A pandas Series after applying the operation.
        """
        pass


class CompositeOperation(Operation):
    def __init__(self, operations=None):
        """
        Initialize the composite operation with an optional list of operations.

        :param operations: A list of TimeseriesOperation instances.
        """
        self.operations = operations if operations is not None else []

    def add_operation(self, operation: Operation):
        """
        Add an operation to the composite.

        :param operation: An instance of a subclass of TimeseriesOperation.
        """
        self.operations.append(operation)

    def process(self, data: pd.Series) -> pd.Series:
        """
        Apply all operations sequentially to the data.

        :param data: A pandas Series representing the timeseries.
        :return: A pandas Series after applying all operations.
        """
        for operation in self.operations:
            data = operation.process(data)
        return data
