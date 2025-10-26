param(
    [Parameter(Mandatory=$true)]
    [string]$Image,

    [Parameter(Mandatory=$true)]
    [string]$ResourceGroup,

    [Parameter(Mandatory=$true)]
    [string]$AppName
)

Write-Host "Deploying image $Image to $AppName in $ResourceGroup"

# Create resource group if not exists
az group create --name $ResourceGroup --location "brazilsouth" | Out-Null

$plan = "$AppName-plan"
# Create App Service plan (Linux)
az appservice plan create --name $plan --resource-group $ResourceGroup --is-linux --sku B1 | Out-Null

# Create webapp for container (if not exists)
$existing = az webapp show --name $AppName --resource-group $ResourceGroup --query "name" -o tsv 2>$null
if (-not $existing) {
    az webapp create --resource-group $ResourceGroup --plan $plan --name $AppName --deployment-container-image-name $Image | Out-Null
} else {
    az webapp config container set --name $AppName --resource-group $ResourceGroup --docker-custom-image-name $Image | Out-Null
}

az webapp restart --name $AppName --resource-group $ResourceGroup | Out-Null

Write-Host "Deployment finished. App URL: https://$AppName.azurewebsites.net"
