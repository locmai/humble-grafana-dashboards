import requests, json, yaml
import os
import shutil


clone_platform_dashboards = {
    'argo-workflow': "https://grafana.com/api/dashboards/13927/revisions/4/download",
    'vault': "https://grafana.com/api/dashboards/12904/revisions/2/download"
}

clone_bootstrap_dashboards = {
    'argocd': 'https://raw.githubusercontent.com/argoproj/argo-cd/master/examples/dashboard.json',
}

clone_system_dashboards = {
    'nginx': 'https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/grafana/dashboards/nginx.json',
    'loki-nginx': 'https://grafana.com/api/dashboards/12559/revisions/11/download',
    'jaeger': 'https://grafana.com/api/dashboards/10001/revisions/2/download',
    'cert-manager': 'https://grafana.com/api/dashboards/11001/revisions/1/download',
}


def clone_dashboards(layer_name:str, clone_dashboards: list):

    if not os.path.exists(f"_json/{layer_name}"):
        os.makedirs(f"_json/{layer_name}")

    for k,v in clone_dashboards.items():
        response = requests.get(v)

        if response.status_code != 200:
                print(f"Skipping the file, response code {response.status_code} not equals 200")
                continue
        else:
            print(f"Downloaded dashboard from {v}")

        with open(f"_json/{layer_name}/{k}.json", 'w') as outfile:
            json.dump(response.json(), outfile)

shutil.rmtree('./_json')

clone_dashboards('platform', clone_platform_dashboards)
clone_dashboards('bootstrap', clone_bootstrap_dashboards)
clone_dashboards('system', clone_system_dashboards)
