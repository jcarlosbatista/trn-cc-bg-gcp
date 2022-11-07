<p align="center">
  <a href="" rel="noopener">
    <img src="https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/images/day1-summary.png" alt="Project logo">
 </a>
</p>


# Summary
Here is the summary of what is going to be covered on this day.

* Introduction and history about the GCP provider
* How storage works on GCP and best practices for a Data Lake
* Ingest data in real-time and the concepts about streaming actions
* The importance of a managed database solution and migration procedures
* Options to move data from different location into GCP


### Google Cloud Platform [GCP]
[Parte 1 - Introdução ao Google Cloud Platform (GCP)](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d1.1_gcp_introduction.excalidraw.png).

- *First Sight at Google Cloud Console*
- *Using GCloud to Interact with Services*
- *Use Python to Interact with Services*
- *Navigate Through The Identity & Access Management*
- *Use Terraform to Build Services*

### first steps on gcp console
```shell
# access console
https://console.cloud.google.com/getting-started?organizationId=132540565286&pli=1&login=true&authuser=1

# overview
- project & billing
- view products
- api
- vpc 
```

### using gcloud to interact with services
```shell
# info
https://cloud.google.com/sdk/gcloud

# gcloud cli cheat sheet
https://cloud.google.com/sdk/docs/cheatsheet

# install gcloud cli
https://cloud.google.com/sdk/docs/install

# init config & validate
gcloud init
gcloud auth list
gcloud config list project

# explore
gcloud --help
gcloud
```

### understanding how to use the google cloud python client
```shell
# google's python client 
https://github.com/googleapis/google-cloud-python/blob/main/README.rst

- available libraries
- examples

# authentication 
https://cloud.google.com/docs/authentication/client-libraries
```

### use python api to spin-up a service
```shell
# virtual env [pycharm]
# install requirements
pip install -r requirements.txt

# interact with bucket
https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/src/d1-intro-ingestion-migration/create_bucket.py
https://cloud.google.com/storage/docs/deleting-buckets#storage-delete-bucket-python
```

### use gcloud to spin-up a service on cloud shell
```shell
# interact with bucket
gcloud storage buckets create gs://owshq-gcloud-landing-zone
gcloud storage buckets delete gs://owshq-gcloud-landing-zone
```

### use terraform to build infrastructure
```shell
# build multi-cloud infrastructure
https://www.terraform.io/
https://registry.terraform.io/

# provider & modules
https://registry.terraform.io/providers/hashicorp/google/latest/docs
https://github.com/hashicorp/terraform-provider-google
```


### Google Cloud Storage
[Parte 2 - Google Cloud Storage (GCS)](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d1.2_gcs.excalidraw.png).

- *Ingestion App to Create Files on GCS*
- *Creating a Google Cloud Storage Bucket*
- *Configure Data Lake using Best Practices*

### ingestion python app [data-gen-datastores]
```python
# google cloud storage
print(GoogleCloudStorage(entity="Users", rows=700).write())
print(GoogleCloudStorage(entity="Transactions", rows=300).write())
print(GoogleCloudStorage(entity="Stocks", rows=100).write())
```

### create gcs buckets for zones using best practices
```shell
# name of the buckets to create
owshq-landing-zone
owshq-processing-zone
owshq-curated-zone
owshq-archive-zone

# bucket creation
# AutoClass Manager
gcloud storage buckets create --help 
```


### Google Cloud Pub/Sub
[Parte 3 - Google Cloud Pub/Sub](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d1.3_pub_sub.excalidraw.png).

- *Publish Messages using Python App for Real-Time Ingestion*
- *Publish & Subscription Types*
- *Pub/Sub to BigQuery*


### publish messages into pub/sub
```shell
# important links
https://cloud.google.com/pubsub/docs/create-subscription

# create & list topics
gcloud pubsub topics create src-py-app-users-events-json
gcloud pubsub topics list

# publish messages
https://cloud.google.com/pubsub/docs/publisher
ingestion-data-stores-app
python3.9 cli.py 'pubsub-music-events'

# housekeeping
gcloud pubsub topics delete src-py-app-users-events-json
```


### publish messages into bigquery
```shell
# create bigquery subscription = sbscpt-big-query
# set permissions to account
service-568528137488@gcp-sa-pubsub.iam.gserviceaccount.com

# create table [OneWaySolution]
# field data as string
events-music

# https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions
SELECT *
FROM `silver-charmer-243611.OneWaySolution.events-music` LIMIT 1000
```

### Google Cloud SQL & DMS
[Parte 4 - Google Cloud SQL & DMS](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d1.4_cloud_sql_dms.excalidraw.png).

- *Walk-Through: Google Cloud SQL*
- *Migrate a Postgres Database to Cloud SQL using DMS*

### Data Transfers
[Parte 5 - Data Transfers](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d1.5_data_transfers.excalidraw.png).

- *Move Data from Blob Storage to GCS using Storage Transfer Service*
- *Transfer from S3 to BigQuery using BigQuery Data Transfer Service*
- *Sync-Up Data from Different Sources into GCS using AirByte*
