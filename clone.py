import requests, json, yaml

clone_platform_dashboards = {
    'argocd': 'https://raw.githubusercontent.com/argoproj/argo-cd/master/examples/dashboard.json',
    'nginx': 'https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/grafana/dashboards/nginx.json',
    'loki-nginx': 'https://grafana.com/api/dashboards/12559/revisions/11/download',
}

def clone_dashboards(layer_name:str, clone_dashboards: list):
    for k,v in clone_dashboards.items():
        response = requests.get(v)

        if response.status_code != 200:
                print(f"Skipping the file, response code {response.status_code} not equals 200")
                continue
        else:
            print(f"Downloaded dashboard from {v}")

        with open(f"_json/{layer_name}/{k}.json", 'w') as outfile:
            json.dump(response.json(), outfile)
        
clone_dashboards('platform', clone_platform_dashboards)
