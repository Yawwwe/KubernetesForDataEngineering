from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark_conn = (SparkSession.builder.appName("SparkProcessing").getOrCreate())

    print("Spark session is ready")

    spark_conn.stop()