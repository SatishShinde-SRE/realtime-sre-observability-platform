Write-Host "Starting order-service container..."

docker compose start order-service

Write-Host "Waiting 10 seconds for service to become healthy..."
Start-Sleep -Seconds 10

Write-Host "Checking health endpoint..."

try {
    Invoke-WebRequest -Uri "http://localhost:5000/health" -UseBasicParsing
    Write-Host "order-service recovered successfully."
} catch {
    Write-Host "Health check failed. Check container logs:"
    Write-Host "docker logs order-service"
}