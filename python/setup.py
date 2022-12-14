#!/usr/bin/env python3

import requests
import os
import sys
import time
import json

try:
    humanitec_token = os.environ['HUMANITEC_TOKEN']
    humanitec_org = os.environ['HUMANITEC_ORG']
    gcp_username = os.environ['INSTRUQT_GCP_PROJECT_GCP_PROJECT_USER_EMAIL']
    gcp_password = os.environ['INSTRUQT_GCP_PROJECT_GCP_PROJECT_USER_PASSWORD']
    gcp_id = os.environ['INSTRUQT_GCP_PROJECT_GCP_PROJECT_PROJECT_ID']
    gcp_sa = os.environ['GCP_SA']
    gke_endpoint = os.environ['GKE_ENDPOINT']
    k8_gcpprojectid = os.environ ['INSTRUQT_GCP_PROJECT_GCP_PROJECT_PROJECT_ID']
    k8_gcpzone = os.environ ['GOOGLE_ZONE']
    random = os.environ ['UNIQUE']
    sql_usr = os.environ ['SQL_USR']
    sql_pass = os.environ ['SQL_PASS']
    sql_connection = os.environ['SQL_CONNECTION']
    
    # gke_payload = os.environ['GKE_PAYLOAD']
    # azure_client_id = os.environ ['RANDOM']
    # azure_client_secret = os.environ ['RANDOM']
    # azure_subscription_id = os.environ ['RANDOM']
    # azure_tenant_id = os.environ ['RANDOM']
    # aks_endpoint = os.environ ['RANDOM']


except Exception as e:
    print(f"Error: Could not read {e} from environment.")
    print(f"Please export {e} as environment variable.")


humanitec_url = "api.humanitec.io"

headers = {
    'Authorization': f'Bearer {humanitec_token}',
    'Content-Type': 'application/json'
}




#Register GCP CloudSQL
#########################################################

url = f"https://{humanitec_url}/orgs/{humanitec_org}/resources/defs"
payload = {
"id": f"postgres-{random}",
"name": f"postgres-{random}",
"type": "postgres",
"driver_type": "humanitec/postgres-cloudsql",
"driver_account": f"{random}",
"driver_inputs": {
  "secrets": {
    "dbcredentials": {
      "password": f"{sql_pass}",
      "username": f"{sql_usr}"
    }
  },
  "values": {
      "instance": f"{sql_connection}"
  }
 } 
}

response = requests.request("POST", url, headers=headers, json=payload)
if response.status_code==200:
    print(f"The resource CloudSQL definition has been registered.")
else:
    print(f"Unable to create CloudSQL resource account. POST {url} returned status code {response.status_code}.")


#Register Namespace
#########################################################

url = f"https://{humanitec_url}/orgs/{humanitec_org}/resources/defs"
payload = {
"id": f"namespace-{random}",
"name": f"namespace-{random}",
"type": "k8s-namespace",
"driver_type": "humanitec/static",
"criteria": [
    {
      "env_type": "development"
    }
  ],
"driver_inputs": {
    "values": {
    "namespace": "${context.env.id}-env-${context.app.id}-app"
    }
  }
} 

response = requests.request("POST", url, headers=headers, json=payload)
if response.status_code==200:
    print(f"The Namespace resource definition has been registered.")
else:
    print(f"Unable to create Namepsace resource definition. POST {url} returned status code {response.status_code}.")
    

