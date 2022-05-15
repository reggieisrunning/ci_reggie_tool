import sys
sys.path.append("..")
from github import github_api
from datetime import *
from dateutil import parser


if __name__ == '__main__':

    since_datetime = datetime.today() - timedelta(days=1)
    since_datetime_midnight = datetime.combine(since_datetime, datetime.min.time())
    since_time = since_datetime_midnight.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    print(since_time)
    issue_list = github_api.get_github_issue_list(owner="Tencent", repo="bk-ci", since=since_time)

    for issue_item in issue_list:
        issue_created_at = parser.parse(issue_item["issue_created_at"])
        if issue_created_at.replace(tzinfo=None) > since_datetime:
            print(issue_item)
