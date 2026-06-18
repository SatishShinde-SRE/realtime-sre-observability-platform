# Real-Time SRE Observability and Incident Response Platform

![SRE Project CI]:- (https://github.com/SatishShinde-SRE/realtime-sre-observability-platform/actions/workflows/ci.yml/badge.svg)

## Overview

This project demonstrates a production-like Site Reliability Engineering workflow using a containerized Order Service and a complete observability stack.

The goal of this project is to show how an SRE monitors service health, detects incidents, investigates issues using metrics and logs, responds using runbooks, and documents incidents using postmortems.

## Architecture

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

## Tech Stack

Application:- 	    Python Flask
Containerization:- 	Docker
Orchestration:- 	Docker Compose
Metrics:- 	        Prometheus
Dashboards:- 	    Grafana
Alerting:-   	    Alertmanager
Logs:- 	            Loki
Log Shipping:- 	    Promtail
Container Metrics:- cAdvisor
System Metrics:- 	Node Exporter
Scripts:- 	        PowerShell

## Features

-Containerized Flask Order Service
-Health check endpoint
-Prometheus metrics endpoint
-Grafana dashboard for service health
-Alertmanager integration
-Loki-based centralized logging
-cAdvisor container metrics
-Node Exporter system metrics
-Incident simulation scripts
-Service recovery script
-SLO and SLI documentation
-Incident runbook
-Postmortem document
-Persistent Docker volumes for Grafana, Prometheus, and Loki

## Application Endpoints

/  :- 	Service information
/health	:- Health check
/order	:- Successful business request
/slow	:- Simulates latency
/error	:- Simulates HTTP 500 error
/metrics	:- Prometheus metrics

## Local URLs

Order Service:-  
	http://localhost:5000
Prometheus:-  
	http://localhost:9090
Grafana:-  
	http://localhost:3000
Alertmanager:-  
	http://localhost:9093
Loki Ready Check:-  
	http://localhost:3100/ready
cAdvisor:-  
	http://localhost:8080
Node Exporter:-  
	http://localhost:9100/metrics


## Grafana login:

Username: admin
Password: admin

## SRE Concepts Demonstrated

SLIs:- 	                Availability, latency, error rate, traffic, saturation
SLOs:- 	                Defined reliability targets for Order Service
Error Budget:- 	        99.9% monthly uptime budget calculation
Four Golden Signals:- 	Latency, traffic, errors, saturation
Monitoring:- 	        Prometheus scraping service and infrastructure metrics
Alerting:- 	            Prometheus alert rules and Alertmanager
Logging:- 	            Promtail shipping Docker logs to Loki
Incident Response:- 	Runbook and recovery script
Postmortem:- 	        Documented outage analysis
Persistence	:-          Docker volumes for Grafana, Prometheus, and Loki

## How To Run The Project

Make sure Docker Desktop is running.

From the project root:

#docker compose up -d --build

Check containers:

#docker ps

Stop containers without deleting data:

#docker compose stop

Start containers again:

#docker compose start

Do not use this unless you intentionally want to remove containers:

#docker compose down

Never use this unless you want to delete stored dashboard, metrics, and logs:

#docker compose down -v


## Incident Simulation Scripts

Run from project root:

.\scripts\generate-load.ps1

.\scripts\simulate-error.ps1

.\scripts\simulate-latency.ps1

.\scripts\simulate-outage.ps1

Recover service:

.\scripts\recover-service.ps1

## Alerts

ServiceDown:-	      Order Service is unavailable
HighErrorRate:-	      More than 5% of requests return 5xx
HighLatency:-	      P95 latency is above 500ms
ContainerHighCPU:-	  Container CPU usage is high
ContainerHighMemory:- Container memory usage is high


## Folder Structure

Realtime-Sre-Project/
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── monitoring/
│   ├── prometheus.yml
│   ├── alert-rules.yml
│   ├── alertmanager.yml
│   ├── loki-config.yml
│   └── promtail-config.yml
├── scripts/
│   ├── generate-load.ps1
│   ├── simulate-error.ps1
│   ├── simulate-latency.ps1
│   ├── simulate-outage.ps1
│   └── recover-service.ps1
├── docs/
│   ├── architecture.md
│   ├── slo-sli.md
│   ├── incident-runbook.md
│   ├── postmortem.md
│   └── screenshots/
├── docker-compose.yml
└── README.md


## Documentation

[Architecture](docs/architecture.md):-	       System design and observability flow
[SLO and SLI](docs/slo-sli.md):-	           Reliability targets and indicators
[Incident Runbook](docs/incident-runbook.md):- Investigation and recovery steps
[Postmortem](docs/postmortem.md):-	           Incident analysis and action items

