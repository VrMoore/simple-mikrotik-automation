# --- config ---
$hostnames = @("www.facebook.com")
$outputFile = ".\scripts\block_site.rsc"

# clear file
"" | Set-Content -Path $outputFile

Write-Host "Saving results to $outputFile`n"

foreach ($hostname in $hostnames) {
    Write-Host "Resolving $hostname ..."

    # Try to resolve A and AAAA records
    $records = @()
    try {
        $records += Resolve-DnsName -Name $hostname -Type A -ErrorAction Stop
    } catch {}

    # Filter valid IPs
    $ips = $records | Where-Object { $_.IPAddress } | Select-Object -ExpandProperty IPAddress -Unique

    if ($ips.Count -gt 0) {
        foreach ($ip in $ips) {
            $line = "ip firewall address-list add list=BlockedWebsites address=$ip comment=`"$hostname`""
            Add-Content -Path $outputFile -Value $line
            Write-Host "  -> Found: $ip"
        }
    } else {
        Write-Host "  -> No IP found for $hostname"
    }

    $line_firewall = "ip firewall filter add chain=forward dst-address-list=BlockedWebsites action=drop"
    Add-Content -Path $outputFile -Value $line_firewall
}

Write-Host " MikroTik script generated at: $outputFile"
