import sys
sys.path.append("..")
import requests
import time
import re
import json
from utils.log_utils import logger


def get_github_issue_list(owner: str="reggieisrunning", repo: str="PyDummyPlugin", **kwargs) -> list:

    base_api_url = "https://api.github.com/repos/{owner}/{repo}/issues".format(owner=owner, repo=repo)
    issue_list = []
    params = kwargs
    if "per_page" not in params:
        params["per_page"] = 100
    if "page" not in params:
        params["page"] = 1

    with open("../git_token", "r") as fd:
        git_token = fd.read()

    headers = {"Authorization": "token {}".format(git_token)}

    while True:
        rsp = requests.get(base_api_url, headers=headers, params=params)
        result = rsp.json()
        if len(result) == 0:
            break
        for issue_item in result:
            try:
                issue_assignee = issue_item["assignee"]["login"] if issue_item["assignee"] is not None else None
                issue_assignees = ",".join(([x["login"] for x in issue_item["assignees"]])) if issue_item[
                                                                                                   "assignees"] is not [] else None
                issue_number, issue_title, = issue_item["number"], issue_item["title"]
                issue_labels = ",".join(([x["name"] for x in issue_item["labels"]]))
                issue_url = issue_item["html_url"]
                issue_created_at = issue_item["created_at"]

                issue_list.append({
                    "issue_number": issue_number,
                    "issue_title": issue_title,
                    "issue_labels": issue_labels,
                    "issue_assignee": issue_assignee,
                    "issue_assignees": issue_assignees,
                    "issue_url": issue_url,
                    "issue_created_at": issue_created_at
                })
            except Exception as ex:
                logger.exception(ex)
                print(result)


        if len(result) < 100:
            break
        params["page"] += 1


    return issue_list


def get_github_issue_detail(owner: str="reggieisrunning", repo: str="PyDummyPlugin", issue_number: int=1) -> dict:
    base_api_url = "https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}".format(owner=owner, repo=repo,
                                                                               issue_number=issue_number)

    with open("../git_token", "r") as fd:
        git_token = fd.read()

    headers = {"Authorization": "token {}".format(git_token)}

    rsp = requests.get(base_api_url, headers=headers)
    rst = rsp.json()
    return rst


if __name__ == '__main__':

    issue_list = (get_github_issue_list(owner="Tencent", repo="bk-ci", state="all"))
    # issue_list = [{"issue_number": 1835}]
    the_issue_detail_dict = {}
    with open("/Users/lianjiezhou/Downloads/issue_detail.txt", "a") as fd:
        for item in issue_list:
            issue_number = item["issue_number"]
            print(issue_number)
            print(issue_number)
            the_issue_detail_dict[issue_number] = get_github_issue_detail(owner="Tencent", repo="bk-ci", issue_number=issue_number)
            fd.write(json.dumps(the_issue_detail_dict[issue_number]))
            fd.write("\n")





    """
    filter_list = [
        ("assignee", "iccengan"),
        ("assignee", "reggieisrunning"),
        ("labels", "review needed")
    ]
    all_issue_list = []
    for filter in filter_list:
        if filter[0] == "assignee":
            issue_list = get_github_issue_list(owner="Tencent",
                                               repo="bk-ci",
                                               assignee=filter[1]
                                               )

        elif filter[0] == "labels":
            issue_list = get_github_issue_list(owner="Tencent",
                                               repo="bk-ci",
                                               labels=filter[1]
                                               )

        all_issue_list.extend(issue_list)
    """

    """
    # iccen和我的issue
    issue_list = get_github_issue_list(owner="Tencent", repo="bk-ci")

    product_issue_list = []
    other_issue_list = []
    will_handle_issue_list = []
    for issue_item in issue_list:
        if re.search("kind/feat/product", issue_item[2]) or re.search("review needed", issue_item[2]) or re.search(
                "kind/enhancement", issue_item[2]):
            if issue_item[3] == "iccengan" or issue_item[3] == "reggieisrunning" or re.search("iccengan",
                                                                                         issue_item[4]) or re.search(
                "reggieisrunning", issue_item[4]):
                    will_handle_issue_list.append(issue_item)

        else:
            other_issue_list.append(issue_item)

    for item in will_handle_issue_list:
        print(item)

    """
    """"""
