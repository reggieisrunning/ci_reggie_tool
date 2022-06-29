import sys
sys.path.append("..")
import requests
import json
from requests.auth import HTTPBasicAuth
import yaml

from utils.log_utils import logger



def get_tapd_stories_list(workspace_id: int=20357512, **kwargs) -> dict:
    tapd_base_url = "http://apiv2.tapd.oa.com/stories"
    params = kwargs
    params["workspace_id"] = workspace_id
    params["limit"] = 200

    with open("../tapd_auth.yml", "r") as fd:
        auth_data = yaml.load(fd)
    basic = HTTPBasicAuth(auth_data["tapd_code"], auth_data["tapd_secret"])

    rsp = requests.get(tapd_base_url, auth=basic, params=params)
    rst = rsp.json()
    return rst

if __name__ == '__main__':
    data = get_tapd_stories_list()
    for item in data["data"]:
        print(json.dumps(item))
        break

