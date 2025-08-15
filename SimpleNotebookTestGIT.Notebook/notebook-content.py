# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "01babc29-5ad2-4646-b1c8-febbefe48e40",
# META       "default_lakehouse_name": "DS_MONITOR_LH",
# META       "default_lakehouse_workspace_id": "cba393b2-3ed0-42fb-bd14-eea430b01e7b",
# META       "known_lakehouses": [
# META         {
# META           "id": "01babc29-5ad2-4646-b1c8-febbefe48e40"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

print("hello world")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM DS_MONITOR_LH.dim_date LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
