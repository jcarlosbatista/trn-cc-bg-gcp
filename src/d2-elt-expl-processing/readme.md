<p align="center">
  <a href="" rel="noopener">
    <img src="https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/images/day2-summary.png" alt="Project logo">
 </a>
</p>


# Summary
Here is the summary of what is going to be covered on this day.

* Munging and preparing data for analysis
* Processing data using the most powerful processing engine
* Understand the concept of Batch and Stream in a unified system
* Develop react pipelines at scale
* Build end to end pipelines using a graphical interface


### Google DataPrep
[Parte 1 - Google DataPrep](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d2.1_data_prep.excalidraw.png).

- *Munging and Preparing Data using DataPrep by Trifacta*

```shell
# save files location
dataprep-staging-90c18422-2e89-4be8-ba33-5d2a4e00bf74

# location
https://clouddataprep.com/home?projectId=silver-charmer-243611

# import data
# google cloud storage & bigquery
define parameterized path
users landing zone & users BigQuery engine

# add to new flow
# build connections
type = mongodb
ip = 45.55.97.53
db = owshq
auth db = admin
user = root

type = postgres
ip = 159.89.244.91:5432
db = owshq
user = postgres

# add recipe
# search for transformations
# unnest objects into colum
users events [BigQuery]

# flow of One Way Solution
* source
mongodb = users [Users from MongoDB]
bigquery = users [Users Event from BigQuery]

* transformations
- unnest objects
- join databases

* output & actions
- running environment (trifacta photon & dataflow)
- json new file every run [gcs]

# validate job history
job 16448067

# folder
dataprep-staging-90c18422-2e89-4be8-ba33-5d2a4e00bf74
```

### Google DataProc
[Parte 2 - Google DataProc](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d2.2_data_proc.excalidraw.png).

- *Deploying and Executing a PySpark App on Google DataProc ServerLess*

[Local PySpark App](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/src/d2-elt-expl-processing/pyspark-yelp-elt-py/local.py)
```shell
# build local spark application
https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/src/d2-elt-expl-processing/pyspark-yelp-elt-py/local.py
```

[Production PySpark using Spark Serverless Engine](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/src/d2-elt-expl-processing/pyspark-yelp-elt-py/py-etl-yelp-reviews.py)
```shell
# deploy on spark serverless engine
https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/src/d2-elt-expl-processing/pyspark-yelp-elt-py/py-etl-yelp-reviews.py
```

### Google DataFlow
[Parte 3 - Google DataFlow](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d2.3_data_flow.excalidraw.png).

- *Writing a Pipeline using Python on Google DataFlow*

```shell

```