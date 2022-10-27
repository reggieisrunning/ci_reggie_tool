import sys
import shutil
sys.path.append("..")
from datetime import datetime
from github import github_api
from dateutil import parser


if __name__ == '__main__':

    since_datetime = datetime.today().astimezone() - datetime.timedelta(days=2)
    since_datetime2 = datetime.today().astimezone() - datetime.timedelta(days=1)
    # since_datetime = datetime(2022, 6, 3, 8, 0, 0, 0).astimezone() - timedelta(days=2)
    # since_datetime2 = datetime(2022, 6, 3, 8, 0, 0, 0).astimezone() - timedelta(days=1)
    print(since_datetime, since_datetime2)
    since_datetime_midnight = datetime.combine(since_datetime, datetime.min.time())
    since_time = since_datetime_midnight.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    print(since_time)
    issue_list = github_api.get_github_issue_list(owner="Tencent", repo="bk-ci", since=since_time)

    shutil.copyfile("../notice_template/get_issue_from_yesterday_email.tpl",
                    "../email/get_issue_from_yesterday_email_{}.html".format(datetime.today().strftime("%Y%m%d")))
    with open("../email/get_issue_from_yesterday_email_{}.html".format(datetime.today().strftime("%Y%m%d")), "a") as fd:
        for issue_item in issue_list:

            issue_created_at = parser.parse(issue_item["issue_created_at"])
            #if issue_created_at.replace(tzinfo=None) > since_datetime2:
            if issue_created_at > since_datetime2:
                fd.write("    <tr>\n")
                issue_number = issue_item["issue_number"]
                issue_title = issue_item["issue_title"]
                issue_labels = issue_item["issue_labels"]
                issue_assignee = issue_item["issue_assignee"]
                issue_assignees = issue_item["issue_assignees"]
                issue_url = issue_item["issue_url"]
                issue_created_at_time = issue_created_at.strftime("%Y-%m-%d %H:%M:%S")
                fd.write("      <td> {} </td>\n".format(str(issue_number)))
                fd.write("      <td> {} </td>\n".format(str(issue_title)))
                fd.write("      <td> {} </td>\n".format(str(issue_labels)))
                fd.write("      <td> {} </td>\n".format(str(issue_assignee)))
                fd.write("      <td> {} </td>\n".format(str(issue_assignees)))
                fd.write("      <td> {} </td>\n".format(str(issue_url)))
                fd.write("      <td> {} </td>\n".format(str(issue_created_at_time)))
                fd.write("    </tr>\n")
                print(issue_item)
        fd.write("</body>")
        print("hehe")
        print("hehe")
