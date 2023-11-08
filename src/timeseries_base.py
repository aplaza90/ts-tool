import pandas as pd


class Timeseries:
    def __init__(self, timeseries: pd.Series, timeseries_id: int):
        """Initializes a new instance of the Timeseries class.

        Args:
            timeseries (pd.Series): A pandas Series representing the timeseries data.
            timeseries_id (int): An integer representing the unique ID of the timeseries.

        """
        self._timeseries_id = timeseries_id
        self._timeseries = timeseries
        self._annotations_df = pd.DataFrame()
        self._attributes = {}

    def add_annotation(self, annotation_series: pd.Series):
        """Adds annotations to the timeseries object.

        This method updates the internal dataframe that holds annotations
        for the timeseries. The index of the annotation_series should align
        with the timeseries data for correct association.

        Args:
            annotation_series (pd.Series): A pandas Series containing the
                annotations to be added. The name of the series will be used
                as the column name in the annotations dataframe.

        Raises:
            TypeError: If the `annotation_series` is not an instance of pd.Series.

        """
        if not isinstance(annotation_series, pd.Series):
            raise TypeError("The annotation_series must be a pandas Series.")
        self._annotations_df[annotation_series.name] = annotation_series

    def add_attributes(self, attributes: dict):
        """Adds attributes from a dictionary to the `self._attributes` dictionary.

        Args:
            attributes (dict): A dictionary of attribute names and values to be added.

        Raises:
            TypeError: If `attributes` is not a dictionary.

        """
        if not isinstance(attributes, dict):
            raise TypeError("The attributes must be a dictionary.")
        self._attributes.update(attributes)

    def get_timeseries(self) -> pd.Series:
        """Retrieves the timeseries data.

        Returns:
            pd.Series: The timeseries data.

        """
        return self._timeseries

    def get_annotations(self) -> pd.DataFrame:
        """Retrieves the annotations of the timeseries.

        Returns:
            pd.DataFrame: A dataframe containing the annotations of the timeseries.

        """
        return self._annotations_df

    def get_attribute(self, key: str):
        """Retrieves a specific attribute value.

        Args:
            key (str): The name of the attribute to retrieve.

        Returns:
            The value of the attribute, or None if the key does not exist.

        """
        return self._attributes.get(key)
