# Kubernetes Deployment

This folder contains Kubernetes manifests for running the Order Service and Prometheus.

## Files

| File | Purpose |
| --- | --- |
| `namespace.yml` | Creates namespace for the project |
| `order-service-deployment.yml` | Deploys Order Service with replicas, probes, and resource limits |
| `order-service-service.yml` | Exposes Order Service using NodePort |
| `prometheus-configmap.yml` | Provides Prometheus scrape configuration |
| `prometheus-deployment.yml` | Deploys Prometheus |
| `prometheus-service.yml` | Exposes Prometheus using NodePort |

## Prerequisites

Install one local Kubernetes tool:

Minikube