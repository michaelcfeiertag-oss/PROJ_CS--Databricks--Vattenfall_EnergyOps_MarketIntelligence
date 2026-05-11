# PREPARE RUNTIME ENVIRONMENT
from pyspark.sql import functions as F


# TRANSFORMER FOR DATAFRAME COLUMN (parametrized) = general context
# TRANSFORMER: IS_NOT_NULL
def filter__dataframe_column__isnotnull(var_column):
    def _transform(df):
        return df.filter(F.col(var_column).isNotNull())
    return _transform

# TRANSFORMER: UPPER, TRIM
def filter__dataframe_column__upper_trim(var_column):
    def _transform(df):
        return df.withColumn(var_column, F.upper(F.trim(F.col(var_column))))
    return _transform


#DEL--needed_for_pattern_of_functions:# filter(F.col("region") == region)
#DEL--needed_for_pattern_of_functions:# filter(F.col("region").isNotNull())


# FILTERS FOR REFERENCE_DATA context = "asset_reference"

# FILTER region
def filter__asset_reference__region(region):
    def _transform(df):
        if region == "ALL":
            return df
        return df.filter(F.col("region") == region)
    return _transform
