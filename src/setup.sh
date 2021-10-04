# az cloud set --name AzureUSGovernment


az login
az account set --s 'Chad Carroll MAG Subscription'

az group create --name KeyVault-PythonQS-rg --location usgovvirginia

az keyvault create --name capython --resource-group KeyVault-PythonQS-rg

export KEY_VAULT_NAME=capython

az keyvault set-policy --name $KEY_VAULT_NAME --upn ccarroll@McsInternalTrials.onmicrosoft.com --secret-permissions delete get list set

