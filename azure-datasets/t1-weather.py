# Databricks notebook source
! pip install azureml-core azureml-opendatasets pandas

# COMMAND ----------

from azureml.opendatasets import NoaaIsdWeather
from datetime import datetime
from dateutil.relativedelta import relativedelta

# COMMAND ----------


end_date = datetime.today()
start_date = datetime.today() - relativedelta(months=1)
isd = NoaaIsdWeather(start_date=start_date, end_date=end_date)
isd_df = isd.to_pandas_dataframe()

# COMMAND ----------


