# import libraries
from pyspark.sql import SparkSession
from pyspark import SparkConf

# main
if __name__ == '__main__':

    # init session
    spark = SparkSession \
            .builder \
            .appName("etl-yelp-py") \
            .getOrCreate()

    # configured parameters
    print(SparkConf().getAll())

    # set log level
    spark.sparkContext.setLogLevel("INFO")

    # spark's flow = input, transform, output
    # input = data lake
    # transform = enrichment
    # output = data lake, mdw
    get_device_file = '/Users/luanmorenomaciel/GitHub/trn-cc-bg-gcp/files/device/*.json'
    get_subscription_file = '/Users/luanmorenomaciel/GitHub/trn-cc-bg-gcp/files/subscription/*.json'

    # 1 = input
    # read data
    df_device = spark.read \
        .format("json") \
        .option("inferSchema", "true") \
        .option("header", "true") \
        .json(get_device_file)

    df_subscription = spark.read \
        .format("json") \
        .option("inferSchema", "true") \
        .option("header", "true") \
        .json(get_subscription_file)

    # print partitions
    print(df_device.rdd.getNumPartitions())
    print(df_subscription.rdd.getNumPartitions())

    # show data
    df_device.show()
    df_subscription.show()

    # count rows
    print(df_device.count())
    print(df_subscription.count())

    # sql
    df_device.createOrReplaceTempView("vw_device")
    df_subscription.createOrReplaceTempView("vw_subscription")

    # 2 = enrichment
    df_join = spark.sql("""
        SELECT device.user_id, 
               device.platform, 
               device.manufacturer,
               subscription.payment_method,
               subscription.plan,
               subscription.subscription_term
        FROM vw_device AS device
        INNER JOIN vw_subscription AS subscription
        ON device.user_id = subscription.user_id
    """)

    df_join.show()

    # 3 = output
    df_join.write.format("parquet").mode("overwrite").save("/Users/luanmorenomaciel/GitHub/trn-cc-bg-gcp/files/enriched")

