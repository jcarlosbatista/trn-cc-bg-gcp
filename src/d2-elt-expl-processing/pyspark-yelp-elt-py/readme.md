# Google Cloud DataProc - [Apache Spark]

### interact with gcs using google [cloud shell]
```sh
# gsutil to list files
gsutil ls gs://owshq-landing-zone/files
gsutil ls gs://owshq-landing-zone/app
```

### interact with gcs using google [cloud shell]
```sh
# create cluster using cli
# name = owshq-apache-spark
# region = us-east1
# zone = us-east1-c
# cluster type = standard
# image type = 2.0-debian10
# component gateway = enable
# machine family = general-purpose
# series = n1
# type = n1-standard-2 [2 vcpus & 7.5 gb] x [2]
# access = allow api access of all gcp services

gcloud dataproc clusters create owshq-apache-spark --enable-component-gateway --region us-east1 --zone us-east1-c --master-machine-type n1-standard-2 --master-boot-disk-size 500 --num-workers 2 --worker-machine-type n1-standard-2 --worker-boot-disk-size 500 --image-version 2.0-debian10 --scopes 'https://www.googleapis.com/auth/cloud-platform' --project silver-charmer-243611
```

### submit a job on dataproc [apache spark]
```sh
# job name = dataproc-batch-etl-yelp-py
# region = us-east1
# cluster name = owshq-luan-moreno
# job type = pyspark
# python file loc = gs://owshq-landing-zone/app/cluster.py

# pyspark job submit process
# https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/pyspark
gcloud dataproc jobs submit pyspark --cluster=owshq-apache-spark py-etl-yelp-reviews.py
gcloud dataproc jobs wait f7101b3e86694ec08bad21d895c20672 --project silver-charmer-243611 --region us-east1

# spark history server
https://uh6z66f5avfz5gkwxj5zux2xxu-dot-us-east1.dataproc.googleusercontent.com/sparkhistory/

# time taken to process
# spin up cluster + execution time
1 min 17 sec
4 min 35 sec
5 min 52 sec

# destroy the cluster
gcloud dataproc clusters delete owshq-apache-spark --region=us-east1
```

### submit a job on dataproc serverless [apache spark]
```sh
# updating gcloud
gcloud components update

# https://cloud.google.com/dataproc-serverless/docs
# https://cloud.google.com/sdk/gcloud/reference/beta/dataproc/batches/submit/pyspark

# enable private google access on subnetwork
# specific region = us-east1
https://cloud.google.com/vpc/docs/configure-private-google-access
https://console.cloud.google.com/networking/networks/list?authuser=1&project=silver-charmer-243611

# cli for serverless apache spark
gcloud dataproc batches submit pyspark --help

# execute pyspark job on serverless spark
/Users/luanmorenomaciel/GitHub/trn-cc-bg-gcp/src/d2-elt-expl-processing/pyspark-yelp-elt-py/

gcloud dataproc batches submit pyspark --help 

gcloud dataproc batches submit pyspark py-etl-yelp-reviews.py \
    --batch=batch-07-py-etl-yelp-reviews --deps-bucket=gs://owshq-code-repository \
    --region=us-east1 --py-files='py-etl-yelp-reviews.py'

# get execution context
gcloud dataproc batches wait batch-07-py-etl-yelp-reviews --project silver-charmer-243611 --region us-east1

# time taken to process
4 min 53 sec

# pricing model
# data compute units (dcus) & shuffle storage
https://cloud.google.com/dataproc-serverless/pricing
```