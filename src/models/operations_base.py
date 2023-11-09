from abc import ABC, abstractmethod

from timeseries_base import Timeseries


class Operation(ABC):
    def __init__(self, name: str):
        """
        Initialize an Operation with a name.

        Args:
            name (str): The name of the operation.
        """
        self.name = name

    @abstractmethod
    def process(self, timeseries: Timeseries) -> None:
        """Processes the timeseries object.

        This method must be overridden by all subclasses to apply an operation
        on the timeseries data and modify its annotations or attributes.

        All the changes in the Timeseries object must be done from this method

        Args:
            timeseries (Timeseries): An instance of the Timeseries class.

        """
        pass


class CompositeOperation(Operation):
    def __init__(self, name: str, operations=None):
        """
        Initialize the composite operation with an optional list of operations.

        Args:
            name (str): The name of the composite operation.
            operations (list of Operation): A list of Operation instances.
        """
        super().__init__(name)
        self.operations = operations if operations is not None else []

    def add_operation(self, operation: Operation):
        """
        Add an operation to the composite.

        Args:
            operation (Operation): An instance of a subclass of Operation.
        """
        if not isinstance(operation, Operation):
            raise TypeError("The operation must be an instance of Operation.")
        self.operations.append(operation)

    def remove_operation(self, operation_name: str):
        """
        Remove an operation from the composite based on its name.

        Args:
            operation_name (str): The name of the operation to be removed.
        """
        self.operations = [op for op in self.operations if op.name != operation_name]

    def process(self, timeseries: Timeseries) -> None:
        """
        Apply all operations sequentially to the timeseries object.

        Args:
            timeseries (Timeseries): An instance of the Timeseries class representing the
             timeseries.
        """
        for operation in self.operations:
            operation.process(timeseries)
