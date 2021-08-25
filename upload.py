import requests, json, os

json_data = {}
with open(f"_json/platform/argocd.json", 'r') as infile:
    json_data = json.load(infile)

gf_api_key = os.environ['GF_API_KEY']

url = 'https://grafana.locmai.dev'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {gf_api_key}"
}

r = requests.post(url, json=json_data, headers=headers)

print(r.status_code)