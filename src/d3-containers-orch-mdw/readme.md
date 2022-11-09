<p align="center">
  <a href="" rel="noopener">
    <img src="https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/images/day2-summary.png" alt="Project logo">
 </a>
</p>


# Summary
Here is the summary of what is going to be covered on this day.

* Understanding Container and how to orchestrate apps 
* Data pipeline orchestration 
* Store apps data at large scale
* Query any shape of data using a MDW engine


### Google GKE & Cloud Run
[Parte 1 - Google GKE & Cloud Run](https://github.com/owshq-plumbers/trn-cc-bg-gcp/blob/main/docs/d2.1_data_prep.excalidraw.png).

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
airflow
postgresql

# install apps 
helm repo update
k create namespace orchestrator

helm upgrade --install airflow apache-airflow/airflow -f /Users/luanmorenomaciel/GitHub/trn-cc-bg-gcp/src/d3-containers-orch-mdw/kubernetes/helm-chart/airflow/values-development.yaml -n orchestrator
helm ls

kubectl port-forward svc/airflow-webserver 8080:8080 -n orchestrator

# housekeeping
helm delete airflow -n orchestrator

k delete pvc data-airflow-postgresql-0
k delete pvc logs-airflow-worker-0
k delete pvc logs-airflow-worker-1
k delete pvc redis-db-airflow-redis-0

k delete namespace orchestrator
```

