# Incident Postmortem: Order Service Outage

## Incident Summary

The Order Service became unavailable during a controlled outage simulation. Prometheus detected the service as down, Alertmanager received the alert, and the service was recovered using the recovery script.

## Date

2026-02-01

## Service

Order Service

## Severity

SEV-2

## Duration

Approximately 5-8 minutes

## Impact

Users were unable to access the Order Service during the simulated outage. Requests to `/health`, `/order`, and `/metrics` failed while the container was stopped.

## Detection

The incident was detected by Prometheus using the following alert rule:

up{job="order-service"} == 0

Prometheus changed the alert state from:

Inactive -> Pending -> Firing

Alertmanager displayed the active ServiceDown alert.

## Detection

Time	Event
10:00	Outage simulation started
10:01	Prometheus target changed to DOWN
10:02	ServiceDown alert moved to Pending
10:03	ServiceDown alert moved to Firing
10:04	Alertmanager received alert
10:05	Recovery script executed
10:06	Service health check passed
10:07	Prometheus target returned to UP
10:08	Alert resolved

## Root Cause

The order-service container was intentionally stopped using the outage simulation script:
.\scripts\simulate-outage.ps1

This was part of planned incident testing.

# Resolution

The service was recovered using:

#.\scripts\recover-service.ps1

The recovery script restarted the service and validated the /health endpoint.

## What Went Well
- Prometheus detected the outage.
- Alertmanager received the alert.
- Grafana dashboard showed service impact.
- Recovery steps were documented.
- Recovery script restored the service quickly.

## What Could Be Improved
- Add automated alert notifications using Slack or email.
- Add Kubernetes liveness and readiness probes.
- Add automated dashboard provisioning.
- Add CI/CD validation for Docker builds.
- Add cloud deployment option.