import sys
sys.path.append("..")
from github import github_api
import re


def judge_is_my(issue, label_list):

    for label_item in label_list:
        try:
            # if re.search(label_item, issue["issue_labels"]) and issue["issue_assignee"] in [ None, "zanyzhao", "iccengan"]:
            #    print(item)
            #    break
            if re.search("iccengan", str(issue["issue_assignee"])):
                print(item)
                break
            if re.search("iccengan", str(issue["issue_assignees"])):
                print(item)
                break

        except Exception as e:
            print("-"*30)
            print(item)
            print("-" * 30)

            raise Exception(e)


if __name__ == '__main__':

    label_list = ["kind/feat/product", "priority/backlog", "review needed", "kind/enhancement"]
    issue_list = github_api.get_github_issue_list(owner="Tencent", repo="bk-ci")
    for item in issue_list:
        judge_is_my(item, label_list)
