from datetime import *
from github import Github


class GitHub:

    def __init__(self, token, organization, repo):
        self.token = token
        self.org = organization

        self.g = Github(token)
        self.repo = self.g.get_repo(organization + "/" + repo)

    def get_open_pr(self):
        pr_list = self.repo.get_pulls(state='open', base='master')
        return pr_list

    def get_closed_pr(self):
        pr_list = self.repo.get_pulls(state='closed', base='master')
        return pr_list

    def get_open_prs_per_branch(self, branch):
        pr_list = self.repo.get_pulls(state='closed', base=branch)
        return pr_list

    # Start & End in format YYYY-MM-DD
    def get_closed_pr_by_date(self, start, end):
        start = datetime.strptime(start, "%Y-%m-%d")
        end = datetime.strptime(end, "%Y-%m-%d")
        pr_closed_list = []
        pr_list = self.repo.get_pulls(state='closed', base='master')
        for pr in pr_list:
            if start.year <= pr.closed_at.year <= end.year:
                if start.month <= pr.closed_at.month <= end.month:
                    if start.day <= pr.closed_at.day <= end.day:
                        pr_closed_list.append(pr)
        return pr_closed_list

    def get_pr_info(self, pr_id):
        pr = self.repo.get_pull(pr_id)
        # Wasn't sure how to get dict info so just made it return some info.
        info = {"title": pr.title, "body": pr.body, "user": pr.user.name, "company": pr.user.company, "state": pr.state,
                "commits": pr.commits, "base": pr.base}
        return info

    def get_approvers(self, pr_id):
        pr = self.repo.get_pull(pr_id)
        approvers = pr.get_review_requests()
        approved_list = []
        for approver in approvers[1]:
            for approved in pr.get_reviews():
                if approver == approved.user:
                    approved_list.append(approved)
        return approved_list

    def get_pending_approvers(self, pr_id):
        pr = self.repo.get_pull(pr_id)
        approvers = pr.get_review_requests()
        approvers = approvers[1]
        approved_list = []
        unapproved_list = []
        for approver in approvers:
            for approved in pr.get_reviews():
                if approver == approved.user:
                    approved_list.append(approved)
        for approver in approvers:
            if approver in approved_list:
                pass
            else:
                unapproved_list.append(approver)
        return unapproved_list

    def get_mergeable(self, pr_id):
        pr = self.repo.get_pull(pr_id)
        return pr.mergeable

    def get_review_comments(self):
        return self.repo.get_pulls_review_comments()

    def merge_pr(self, pr_id, title, message):
        pr = self.repo.get_pull(pr_id)
        if self.get_mergeable(pr_id):
            pr.merge(message, title)

    def check_pr_desc(self, pr_id):
        pr = self.repo.get_pull(pr_id)
        if pr.body == '':
            pr.edit(state=closed)

    def add_pr_check(self, branch, state, url, description, context):
        sha = self.repo.get_git_ref(branch).object.sha
        self.repo.get_commit(sha=sha).create_status(state=state, target_url=url, description=description, context=context)

    def add_comment(self, pr_id, message, commit_id, path, position):
        pr = self.repo.get_pull(pr_id)
        pr.create_comment(message, commit_id, path, position)

    def approve_pr(self, pr_id, commit, body, event, comments):
        pr = self.repo.get_pull(pr_id)
        pr.create_review(commit=commit, body=body, event=event, comments=comments)

    def new_branch(self, branch_name):
        sha = self.repo.get_git_ref('master').object.sha
        self.repo.create_git_ref(ref='refs/heads/' + branch_name, sha=sha)

    def del_branch(self, branch_name):
        ref = self.repo.get_git_ref(branch_name)
        ref.delete()
