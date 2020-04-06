import requests

CONTRIBUTING_URL = 'https://gist.githubusercontent.com/PurpleBooth/b24679402957c63ec426/raw/5c4f62c1e50c1e6654e76e873aba3df2b0cdeea2/Good-CONTRIBUTING.md-template.md'


def get_contributing_md():
    response = requests.get(CONTRIBUTING_URL)
    return response.content.decode('utf-8')
