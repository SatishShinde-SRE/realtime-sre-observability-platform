param(
    [int]$Requests = 30
)

Write-Host "Generating error traffic to /error endpoint..."

1..$Requests | ForEach-Object {
    try {
        Invoke-WebRequest -Uri "http://localhost:5000/error" -UseBasicParsing | Out-Null
    } catch {
        Write-Host "Expected error request $_ generated"
    }
}

Write-Host "Finished generating error traffic."