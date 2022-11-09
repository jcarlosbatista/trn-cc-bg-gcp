<p align="center">
  <a href="" rel="noopener">
    <img src="https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/images/day3-summary.png" alt="Project logo">
 </a>
</p>


# Summary
Here is the summary of what is going to be covered on this day.

* Understanding container and how to orchestrate apps 
* Data pipeline orchestration 
* Store apps data at large scale
* Query any shape of data using a MDW engine


### Google GKE & Cloud Run
[Parte 1 - Google GKE & Cloud Run](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d3.1_gke_cloud_run.excalidraw.png).

- *Deploying Big Data Products on Google Kubernetes Engine (GKE)*
- *Deploy a Python App using Cloud Run for Lightweight Data Transformation*

### google kubernetes engine
```shell
# spin up gke cluster
https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview

standard = pay per node (kubernetes cluster with node configuration flexibility)
autopilot = pay per pod (optimized kubernetes cluster with a hands-off experience)

name = gke-autopilot-owshq-dev

# provision autopilot cluster
gcloud container --project "silver-charmer-243611" clusters create-auto "gke-autopilot-owshq-dev" \
  --region "us-central1" \
  --release-channel "regular" \
  --network "projects/silver-charmer-243611/global/networks/default" \
  --subnetwork "projects/silver-charmer-243611/regions/us-central1/subnetworks/default" \
  --cluster-ipv4-cidr "/17" \
  --services-ipv4-cidr "/22"

# get credentials
# https://cloud.google.com/blog/products/containers-kubernetes/kubectl-auth-changes-in-gke
gcloud components update
gcloud components install gke-gcloud-auth-plugin

gcloud container clusters get-credentials gke-autopilot-owshq-dev --region us-central1 --project silver-charmer-243611

# basics of kubernetes
kubectx gke_silver-charmer-243611_us-central1_gke-autopilot-owshq-dev
k get nodes
k get sc

# deploy airflow engine
# helm
https://helm.sh/

# artifact hub
https://artifacthub.io/

# verify charts
mongodb

# install apps 
k create namespace database
helm install mongodb bitnami/mongodb -f /Users/luanmorenomaciel/GitHub/trn-cc-bg-gcp/src/d3-containers-orch-mdw/kubernetes/helm-chart/mongodb/values-development.yaml -n database

kubens database
kgp

# Orion platform by One Way Solution

# delete cluster
gcloud container --project "silver-charmer-243611" clusters delete "gke-autopilot-owshq-dev" --region "us-central1"
```

### google cloud run
```shell
# https://cloud.google.com/run/docs/quickstarts
quickstar manuals

# deploy python app into cloud run
https://cloud.google.com/run/docs/overview/what-is-cloud-run
https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service

# https://github.com/owshq-plumbers/trn-cc-bg-gcp/tree/main/src/d3-containers-orch-mdw/app
main.py
requirements.txt
Dockerfile
.dockerignore

# access folder and use the run command
# automatically builds a container image from source and deploy
# skaffold if you use kubernetes

# build the artifact registry docker
gcloud run deploy --help
gcloud run deploy owshq-py-webapp --region "us-central1"

https://owshq-py-webapp-gtptrhetka-uc.a.run.app
# cloud run does not charge when the service is not in use

# obs: set up continuous deployment

# logs
https://console.cloud.google.com/cloud-build/builds/b8e8763a-e847-49dc-932e-169fa94a38f1?project=568528137488

# housekeeping
gcloud run services delete owshq-py-webapp --region "us-central1"
```

### Google Cloud Composer
[Parte 2 - Google Cloud Composer](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d3.2_cloud_composer.excalidraw.png).

- *The DAG Skeleton: The Basics of Apache Airflow*
- *Authoring & Scheduling Data Pipelines Efficiently*
- *CI/CD Strategy to Build DAGs using Composer*

```shell
# create composer service
# enable cloud composer api
https://cloud.google.com/composer/pricing#sku-composer-2

# ui (kubernetes)
environment = composer 2 (Apache Airflow)
name = owshq-composer-development
region = us-central1
image = composer-2.0.30-airflow-2.3.3
sizes = small, medium, large and custom

# guides
https://cloud.google.com/composer/docs/composer-2/run-apache-airflow-dag

# add extra packages 
```

```shell
# build first dag = skeleton
```

```shell
# authoring & scheduling na gcp pipeline
```

```shell
# ci/cd for dag development
```

### Google Cloud BigTable
[Parte 3 - Google Cloud BigTable](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d3.2_cloud_composer.excalidraw.png).

- *Building a Scalable Pipeline of Real-Time Events using Google BigTable as Storage*

```shell
# bigtable = sub 10ms latency on requests

# examples
https://cloud.google.com/bigtable/docs/writing-data#python
https://cloud.google.com/bigtable/docs/writes#simple
https://itnext.io/pubsub-to-bigtable-piping-your-data-stream-in-via-gcp-cloud-functions-a2ef785935b5

# implementers
* python
* cloud functions
* dataflow
```

### Google BigQuery
[Parte 4 - Google BigQuery](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/).

- *Load Files from Storage [GCS] (JSON) into BigQuery*
- *Create a clustered table faster access*
- *Build snapshot of a table*
- *Build materialized views*
- *Query external data sources*

### load local files
```shell
# how to guides
how-to-guides
https://cloud.google.com/bigquery/docs/how-to

# bigquery ui
https://console.cloud.google.com/bigquery

# cli for the big query engine
bq --help

# https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json
# users
bq load \
--source_format=NEWLINE_DELIMITED_JSON --autodetect \
OneWaySolution.yelp-users-json \
gs://owshq-landing-zone/files/users/yelp_academic_dataset_user_2021.json

# reviews
bq load \
--source_format=NEWLINE_DELIMITED_JSON --autodetect \
OneWaySolution.yelp-reviews-json \
gs://owshq-landing-zone/files/reviews/yelp_academic_dataset_review_1.json

# delete bigquery tables
OneWaySolution.yelp-users-json
OneWaySolution.yelp-reviews-json
```

```sql
SELECT COUNT(*) 
FROM `silver-charmer-243611.OneWaySolution.yelp-users-json`;

SELECT COUNT(*) 
FROM `silver-charmer-243611.OneWaySolution.yelp-reviews-json`;
```

### build clustered table
```sql
-- improve query performance and reduce query costs.
-- queries commonly filter on particular columns
-- filter on columns that have many distinct values
-- strict cost estimates before query execution
-- automatic reclustering = performs automatic reclustering in the background
SELECT *
FROM `silver-charmer-243611.OneWaySolution.yelp-reviews-json`
LIMIT 10;

-- 2019-02-17
SELECT DATE(date), COUNT(*) AS q
FROM `silver-charmer-243611.OneWaySolution.yelp-reviews-json`
GROUP BY DATE(date)
ORDER BY q DESC;


CREATE TABLE `silver-charmer-243611.OneWaySolution.clustered-yelp-reviews`
(
  date TIMESTAMP,
  useful INTEGER,
)
CLUSTER BY date AS 
(
  SELECT date, useful FROM `silver-charmer-243611.OneWaySolution.yelp-reviews-json`
);

SELECT *
FROM `silver-charmer-243611.OneWaySolution.clustered-yelp-reviews`
WHERE date BETWEEN '2019-04-01' AND '2019-04-30'
  AND useful <> 0;

-- delete bigquery tables
silver-charmer-243611.OneWaySolution.clustered-yelp-reviews
```

### snapshot table
```sql
-- table snapshot preserves the contents of a table (called the base table) at a particular time
-- save a snapshot of a current table, or create a snapshot of a table as it was at any time in the past seven days
-- one hour ago 
CREATE SNAPSHOT TABLE `silver-charmer-243611.OneWaySolution.yelp-reviews-snapshot`
CLONE `silver-charmer-243611.OneWaySolution.yelp_reviews`
FOR SYSTEM_TIME AS OF TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR);

SELECT *
FROM `silver-charmer-243611.OneWaySolution.yelp-reviews-snapshot`
LIMIT 10;
```

### materialized view
```sql
-- https://cloud.google.com/bigquery/docs/materialized-views-intro
-- materialized views are precomputed views that periodically cache the results of a query for increased performance and efficiency
-- zero maintenance, fresh data
-- smart tuning = reroutes the query to use the materialized view for better performance and efficiency
CREATE MATERIALIZED VIEW `silver-charmer-243611.OneWaySolution.m-view-reviews-per-user`
AS 
(
SELECT users.user_id, 
       SUM(users.review_count) AS reviews,
       COUNT(reviews.stars) AS stars
FROM `silver-charmer-243611.OneWaySolution.yelp-users-json` AS users
INNER JOIN `silver-charmer-243611.OneWaySolution.yelp-reviews-json` AS reviews
ON users.user_id = reviews.user_id
GROUP BY users.user_id
);

SELECT *
FROM `silver-charmer-243611.OneWaySolution.m-view-reviews-per-user`
LIMIT 10;
```