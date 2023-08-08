"""
This module defines the following routines used by the 'split' step of the regression recipe:

- ``create_dataset_filter``: Defines customizable logic for filtering the training
  datasets produced by the data splitting procedure. Note that arbitrary transformations
  should go into the transform step.
"""

from pandas import DataFrame, Series

def custom_split(df):
 """   
 from pandas import Series
    splits = Series("TRAINING", index=range(len(df)))
    # 3rd quarter is validation data
    splits[df["year"] >= 3] = "VALIDATION"
    # 4th quarter is testing data
    splits[df["year"] >= 4] = "TEST"
    return splits 
  """
pass

def create_dataset_filter(dataset: DataFrame) -> Series(bool):
    """
    Mark rows of the split datasets to be additionally filtered. This function will be called on
    the training datasets.

    :param dataset: The {train,validation,test} dataset produced by the data splitting procedure.
    :return: A Series indicating whether each row should be filtered
    """
    # FIXME::OPTIONAL: implement post-split filtering on the dataframes, such as data cleaning.

    return (
        (dataset["fare_amount"] > 0)
        & (dataset["trip_distance"] < 400)
        & (dataset["trip_distance"] > 0)
        & (dataset["fare_amount"] < 1000)
    ) | (~dataset.isna().any(axis=1))
