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

### Google Cloud Storage
[Parte 2 - Google Cloud Storage (GCS)](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d1.2_gcs.excalidraw.png).

- *Ingestion App to Create Files on GCS*
- *Creating a Google Cloud Storage Bucket*
- *Configure Data Lake using Best Practices*


### Google Cloud Pub/Sub
[Parte 3 - Google Cloud Pub/Sub](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d1.3_pub_sub.excalidraw.png).

- *Publish Messages using Python App for Real-Time Ingestion*
- *Publish & Subscription Types*
- *Pub/Sub to BigQuery*

### Google Cloud SQL & DMS
[Parte 4 - Google Cloud SQL & DMS](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d1.4_cloud_sql_dms.excalidraw.png).

- *Walk-Through: Google Cloud SQL*
- *Migrate a Postgres Database to Cloud SQL using DMS*

### Data Transfers
[Parte 5 - Data Transfers](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d1.5_data_transfers.excalidraw.png).

- *Move Data from Blob Storage to GCS using Storage Transfer Service*
- *Transfer from S3 to BigQuery using BigQuery Data Transfer Service*
- *Sync-Up Data from Different Sources into GCS using AirByte*
