# Architecture

## Project Overview

This project is a real-time SRE observability and incident response platform for a demo Order Service.

The goal is to demonstrate how an SRE monitors a production-like service, detects incidents, investigates issues, and performs recovery.

## Architecture Diagram

User / Load Scripts
        |
        v
Order Service (Flask App)
        |
        | exposes /metrics
        v
Prometheus
        |
        | sends alerts
        v
Alertmanager

Order Service Logs
        |
        v
Promtail
        |
        v
Loki
        |
        v
Grafana

cAdvisor ------------> Prometheus
Node Exporter -------> Prometheus
Prometheus ----------> Grafana


****************************************************************

## Component & Perpose

Order Service: - Demo Flask API used as the monitored application
Docker:-         Runs the application and monitoring tools in containers
Docker Compose:- Manages all services together
Prometheus:-     Scrapes and stores metrics
Grafana:-        Displays dashboards for metrics and logs
Alertmanager:-   Receives and displays Prometheus alerts
Loki:-           Stores application logs
Promtail:-       Sends Docker container logs to Loki
cAdvisor:-       Provides container CPU and memory metrics
Node Exporter:-  Provides system-level metrics from the Docker Linux environment

*****************************************************************

## Application Endpoints

/:-        Basic service information
/health:-  Health check endpoint
/order:-   Normal successful business request
/slow:-    Simulates high latency
/error:-   Simulates HTTP 500 errors
/metrics:- Prometheus metrics endpoint

******************************************************************

## Observability Flow

- Prometheus scrapes metrics from the Order Service, cAdvisor, and Node Exporter.
- Grafana queries Prometheus to display metrics dashboards.
- Promtail collects container logs from Docker.
- Loki stores logs.
- Grafana queries Loki to display application logs.
- Prometheus evaluates alert rules.
- Alertmanager receives alerts when incidents occur.

******************************************************************

## Incident Flow

Incident happens
    |
    v
Metric or log changes
    |
    v
Prometheus alert rule triggers
    |
    v
Alertmanager receives alert
    |
    v
SRE checks Grafana dashboard and Loki logs
    |
    v
SRE follows runbook
    |
    v
Service is recovered
    |
    v
Postmortem is written


******************************************************************

## Local URLs

Order Service:-  	 http://localhost:5000
Prometheus:- 	     http://localhost:9090
Grafana:- 	         http://localhost:3000
Alertmanager:-       http://localhost:9093
Loki Ready Check:- 	 http://localhost:3100/ready
cAdvisor:-           http://localhost:8080
Node Exporter:- 	 http://localhost:9100/metrics

