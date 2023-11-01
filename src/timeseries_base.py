from abc import ABC, abstractmethod
import pandas as pd


class AbstractTimeseries(ABC):
    def __init__(self, series: pd.Series, timeseries_id: int):
        """
        Initialize the AbstractTimeseries with a pandas Series and an ID.

        :param series: A pandas Series representing the timeseries data.
        :param timeseries_id: An integer representing the unique ID of the timeseries.
        """
        self.series = series
        self.timeseries_id = timeseries_id
        self.annotations = pd.DataFrame()
        self.attributes = {}

    @abstractmethod
    def add_annotation(self, annotation: pd.DataFrame):
        """
        Add annotations to the timeseries object. Must be implemented by subclasses.

        :param annotation: A pandas DataFrame with annotations.
        """
        pass

    @abstractmethod
    def add_attribute(self, key: str, value):
        """
        Add an attribute resulting from a rule application. Must be implemented by subclasses.

        :param key: The name of the attribute.
        :param value: The value of the attribute, can be a single value or a Series.
        """
        pass

    def get_series(self) -> pd.Series:
        """
        Get the timeseries data.

        :return: The pandas Series of the timeseries data.
        """
        return self.series

    def get_annotations(self) -> pd.DataFrame:
        """
        Get the annotations of the timeseries.

        :return: A pandas DataFrame of the annotations.
        """
        return self.annotations

    def get_attribute(self, key: str):
        """
        Get a specific attribute value.

        :param key: The name of the attribute to retrieve.
        :return: The value of the attribute.
        """
        return self.attributes.get(key)
