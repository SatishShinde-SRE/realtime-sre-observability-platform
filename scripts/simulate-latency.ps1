param(
    [int]$Requests = 10
)

Write-Host "Generating slow traffic to /slow endpoint..."

1..$Requests | ForEach-Object {
    Invoke-WebRequest -Uri "http://localhost:5000/slow" -UseBasicParsing | Out-Null
    Write-Host "Slow request $_ completed"
}

Write-Host "Finished generating slow traffic."