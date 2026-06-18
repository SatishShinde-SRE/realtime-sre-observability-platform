# Incident Runbook

## Purpose

This runbook explains how to investigate and recover from common Order Service incidents.

## Incident 1: ServiceDown

### Alert

ServiceDown

## Severity

- Critical

## Symptoms

- Prometheus target shows DOWN
- Grafana Service Up panel shows 0
- Users cannot access the service
- Alertmanager shows a critical alert

## Investigation Steps

Open Prometheus targets: http://localhost:9090/targets

Check if order-service is DOWN.

Check container status:

#docker ps

Check service logs:

#docker logs --tail 50 order-service

Open Grafana dashboard and check request traffic, errors, and logs.

## Recovery Steps

Start the service:

#docker compose start order-service

Validate health endpoint: http://localhost:5000/health

Confirm Prometheus target is UP.

Confirm Alertmanager alert is resolved.

Monitor Grafana for 5-10 minutes.


### Incident 2: HighErrorRate

# Alert
HighErrorRate

# Severity
Warning

# Symptoms

- Error Requests panel increases
- /error endpoint returns HTTP 500
- Loki logs show ERROR
- Alertmanager receives HighErrorRate alert

## Investigation Steps

Open Grafana dashboard.

Check Error Requests panel.

Open Explore in Grafana.

Select Loki.

Run: {container="order-service"} |= "ERROR"

Check whether errors are isolated or continuous.

## Recovery Steps

Stop error simulation.

Confirm error rate decreases.

Check service logs.

Continue monitoring until alert resolves.

## Incident 3: HighLatency

# Alert
HighLatency

# Severity
Warning

# Symptoms
- P95 Latency panel increases
- /slow endpoint takes around 2 seconds
- Users experience slow response time

## Investigation Steps

Open Grafana dashboard.

Check P95 Latency panel.

Check request rate to understand traffic volume.

Check container CPU and memory panels.

Check logs for slow requests.

## Recovery Steps

Stop latency simulation.

Confirm P95 latency returns to normal.

Monitor service health and error rate.

## Incident 4: Container Resource Saturation

# Alerts
ContainerHighCPU
ContainerHighMemory

# Severity
Warning

# Symptoms
- Container CPU panel increases
- Container memory panel increases
- Service latency may increase

## Investigation Steps
Open Grafana dashboard.

Check Container CPU and Container Memory panels.

Open cAdvisor: http://localhost:8080

Check container-level resource usage.

## Recovery Steps

Reduce traffic or stop load simulation.

Restart service if required.

Monitor CPU and memory for stability.

## Escalation

Escalate if:

 - Service does not recover
 - Alerts keep firing
 - Container repeatedly crashes
 - CPU or memory remains high