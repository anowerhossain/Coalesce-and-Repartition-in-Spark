from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Coalesce vs Repartition Example") \
    .getOrCreate()

# Create a Sample DataFrame with 6 partitions
data = [(i, f"Value_{i}") for i in range(1, 21)]
df = spark.createDataFrame(data, ["id", "value"])
print(df)

# Show initial partitions
print(f"Initial Partitions: {df.rdd.getNumPartitions()}")

# 🔄 Repartition Example (Increase partitions to 10)
df_repartitioned = df.repartition(10)
print(f"Partitions after repartition(10): {df_repartitioned.rdd.getNumPartitions()}")

# 🔽 Coalesce Example (Reduce partitions to 2)
df_coalesced = df.coalesce(2)
print(f"Partitions after coalesce(2): {df_coalesced.rdd.getNumPartitions()}")

# Show sample data
df.show()
df_repartitioned.show()
df_coalesced.show()

# Stop the Spark session
spark.stop()
