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
