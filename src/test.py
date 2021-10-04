from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
import os
# import os
# from azure.mgmt.resource import ResourceManagementClient
# from azure.mgmt.storage import StorageManagementClient
# from azure.mgmt.storage.models import (
#     StorageAccountCreateParameters,
#     StorageAccountUpdateParameters,
#     Sku,
#     SkuName,
#     Kind
# )

# set AZURE_SUBSCRIPTION_ID="65c61e02-d55a-493f-9f4f-741a6cfc0c49"

AZURE_SUBSCRIPTION_ID="0a7ac580-9e64-426b-a0bd-6cd969e735c3"
AZURE_TENANT_ID="72f988bf-86f1-41af-91ab-2d7cd011db47"

# #AZURE_SUBSCRIPTION_ID='65c61e02-d55a-493f-9f4f-741a6cfc0c49'
# # Acquire a credential object using CLI-based authentication.
# credential = AzureCliCredential()

# client = ResourceManagementClient(credential, AZURE_SUBSCRIPTION_ID)
# # storage_client=

# # Retrieve the list of resource groups
# group_list = client.resource_groups.list()

# RESOURCEGROUP='python'
# exits= client.resource_groups.check_existence('k8')

# if client.resource_groups.check_existence(RESOURCEGROUP):
#     print (f"Resource Group {RESOURCEGROUP} exits ")
# else:
#     print (f"Resource Group {RESOURCEGROUP} does not exists.  Creating now...")
#     resource_group_params = {'location':'westus'}
#     client.resource_groups.create_or_update(RESOURCEGROUP,resource_group_params)
#     print (f"Resource Group successfully created.")


# key_vault_params = {
#     'location': 'westus',
#     'properties':  {
#         'sku': {'family': 'A', 'name': 'standard'},
#         'tenantId': os.environ['AZURE_TENANT_ID'],
#         'accessPolicies': [],
#         'enabledForDeployment': True,
#         'enabledForTemplateDeployment': True,
#         'enabledForDiskEncryption': True
#     }
# }

# VAULTNAME='kvtestca123'

# if client.resources.check_existence(RESOURCEGROUP, 'Microsoft.KeyVault',
#                                   '',
#                                   'vaults',
#                                   VAULTNAME,
#                                   '2021-04-01'):
#     print (f"Key Vault {VAULTNAME} exits ")
# else:
#     client.resources.begin_create_or_update(RESOURCEGROUP, 'Microsoft.KeyVault',
#                                     '',
#                                     'vaults',
#                                     'azureSampleVault',
#                                     '2021-06-01-preview',
#                                     key_vault_params)

# Key Vault


# # Show the groups in formatted output
# column_width = 40

# print("Resource Group".ljust(column_width) + "Location")
# print("-" * (column_width * 2))

# for group in list(group_list):
#     print(f"{group.name:<{column_width}}{group.location}")