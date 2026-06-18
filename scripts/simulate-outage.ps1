Write-Host "Stopping order-service container to simulate outage..."

docker compose stop order-service

Write-Host "order-service stopped."
Write-Host "Wait 1-2 minutes, then check:"
Write-Host "Prometheus alerts: http://localhost:9090/alerts"
Write-Host "Alertmanager: http://localhost:9093"
Write-Host "To recover, run: .\scripts\recover-service.ps1"