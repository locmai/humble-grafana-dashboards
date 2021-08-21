import requests, json

clone_platform_dashboards = {
    'argocd': 'https://raw.githubusercontent.com/argoproj/argo-cd/master/examples/dashboard.json'
}

def clone_dashboards(layer_name:str, clone_dashboards: list):
    for k,v in clone_dashboards.items():
        response = requests.get(v)

        if response.status_code != 200:
                print('Skipping the file, response code %s not equals 200' % response.status_code)
                continue

        with open(f"_json/{layer_name}/{k}.json", 'w') as outfile:
            json.dump(response.json(), outfile)

clone_dashboards('platform', clone_platform_dashboards)