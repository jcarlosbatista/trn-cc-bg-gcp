<p align="center">
  <a href="" rel="noopener">
    <img src="https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/images/day4-summary.png" alt="Project logo">
 </a>
</p>


# Summary
Here is the summary of what is going to be covered on this day.

* Unification of the Data Warehouse and the Data Lake systems
* React to data in real-time using CDC changes
* Data fabric to oversee your data assets
* Distributed and global distributed database engine
* Improving postgres database engine


### Google BigLake
[Parte 1 - Google BigLake](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d4.1_big_lake.excalidraw.png).

- *Accessing Data using The BigQuery Omni Engine*
- *Accessing Data on BigLake using The Apache Spark Engine*

### bigquery omni
```shell
# bigquery connectors
# https://cloud.google.com/bigquery/docs/omni-introduction
# https://github.com/GoogleCloudDataproc/spark-bigquery-connector

# access data living on azure
# https://cloud.google.com/bigquery/docs/omni-azure-create-connection#create-azure-tenant
# https://cloud.google.com/bigquery/docs/omni-azure-create-external-table

# 1 = google gcp
explorer - add data
connections to external data sources
connection type = biglake on azure via bigquery omni
name = bl-azr-adls2-owshqblobstg
connection location = azure-eastus2
tenant id = (azure active directory)
 
# 2 = microsoft azure
# azure active directory
# find on bigquery ui [azure app name]
connection info for [bl-azr-adls2-owshqblobstg]
create service principal
adls2 = owshqblobstg
access = storage blob data contributor (iam)
azure app name = bigquery-c8c33e27-a916-4772-a540-d11a33d1b486
```

```sql
CREATE SCHEMA MicrosoftAzure
OPTIONS 
(
  location = 'azure-eastus2'
);


CREATE EXTERNAL TABLE `MicrosoftAzure.yellow_tripdata_2017`
WITH CONNECTION `projects/silver-charmer-243611/locations/azure-eastus2/connections/bl-azr-adls2-owshqblobstg`
OPTIONS 
(
    format = 'CSV', 
    uris = ['azure://owshqblobstg.blob.core.windows.net/stgfiles/nyc-tlc/yellow_tripdata_2017-01.csv']
);


SELECT *
FROM MicrosoftAzure.yellow_tripdata_2017
LIMIT 10;

/*
CREATE OR REPLACE ROW ACCESS POLICY get_limited_trips 
ON MicrosoftAzure.yellow_tripdata_2017
GRANT TO ('user:[YOUR IDENTITY]')
FILTER USING (country = 'US');
*/
```

`
### biglake & apache spark engine
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder \
 .appName('big-lake-query-api') \
 .config('spark.jars', 'gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12–0.24.2.jar') \
 .getOrCreate()
df = spark.read \
 .format('bigquery') \
 .load('MicrosoftAzure.yellow_tripdata_2017')
df.show()
```