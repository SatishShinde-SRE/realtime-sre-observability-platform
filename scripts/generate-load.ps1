param(
    [int]$Requests = 50
)

Write-Host "Generating normal traffic to /order endpoint..."

1..$Requests | ForEach-Object {
    Invoke-WebRequest -Uri "http://localhost:5000/order" -UseBasicParsing | Out-Null
    Write-Host "Normal request $_ completed"
}

Write-Host "Finished generating normal traffic."