$pathsToDelete = @(
    ".tmp.driveupload",
    ".vs",
    "venv",
    "desktop.ini",
    "Thumbs.db"
)

foreach ($path in $pathsToDelete) {
    if (Test-Path $path) {
        try {
            Remove-Item -Recurse -Force $path
            Write-Host "Deleted $path successfully" -ForegroundColor Green
        } catch {
            Write-Host "Failed to delete $path: $($_)" -ForegroundColor Red
        }
    } else {
        Write-Host "$path does not exist" -ForegroundColor Yellow
    }
}
