$($(python .\hostname\get_hostname.py '<user>' '<password>')  | ConvertFrom-Json).statics 
    | where {$_.mac -eq $(python .\network\getmac.py)}
