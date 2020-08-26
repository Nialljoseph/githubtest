from datetime import datetime
from github import Github


class GitHubAPI:

    def __init__(self, token, organization, repo):
        self.token = token
        self.org = organization

        self.token = Github(token)
        self.repo = self.token.get_repo(organization + "/" + repo)

    """Returns a list of open prs"""
    def get_open_pr(self):
        pr_list = self.repo.get_pulls(state='open', base='master')
        return pr_list

    """Returns a list of closed prs"""
    def get_closed_pr(self):
        pr_list = self.repo.get_pulls(state='closed', base='master')
        return pr_list

    """Returns a list of open prs depending on the branch"""
    def get_open_prs_per_branch(self, branch):
        pr_list = self.repo.get_pulls(state='open', base=branch)
        return pr_list

    """Returns a list of closed prs depending on the start and end date"""
    # Start & End in format YYYY-MM-DD
    def get_closed_pr_by_date(self, start, end):
        start = datetime.strptime(start, "%Y-%m-%d")
        end = datetime.strptime(end, "%Y-%m-%d")
        pr_closed_list = []
        pr_list = self.repo.get_pulls(state='closed', base='master')
        for pull_request in pr_list:
            if start.year <= pull_request.closed_at.year <= end.year:
                if start.month <= pull_request.closed_at.month <= end.month:
                    if start.day <= pull_request.closed_at.day <= end.day:
                        pr_closed_list.append(pr)
        return pr_closed_list

    """Returns a dict of misc info for a pr"""
    def get_pr_info(self, pr_id):
        pull_request = self.repo.get_pull(pr_id)
        # Wasn't sure how to get dict info so just made it return some info.
        info = {"title": pull_request.title, "body": pull_request.body, "user": pull_request.user.name, "company": pull_request.user.company, "state": pull_request.state,
                "commits": pull_request.commits, "base": pull_request.base}
        return info

    """Returns a list of requested reviewers"""
    def get_approvers(self, pr_id):
        pull_request = self.repo.get_pull(pr_id)
        approvers = pull_request.get_review_requests()
        approved_list = []
        for approver in approvers[1]:
            for approved in pull_request.get_reviews():
                if approver == approved.user:
                    approved_list.append(approved)
        return approved_list

    """Returns a list of requested reviewers who have not responded"""
    def get_pending_approvers(self, pr_id):
        pull_request = self.repo.get_pull(pr_id)
        approvers = pull_request.get_review_requests()
        approvers = approvers[1]
        approved_list = []
        unapproved_list = []
        for approver in approvers:
            for approved in pull_request.get_reviews():
                if approver == approved.user:
                    approved_list.append(approved)
        for approver in approvers:
            if approver in approved_list:
                pass
            else:
                unapproved_list.append(approver)
        return unapproved_list

    """Returns whether or not a pr is mergeable"""
    def get_mergeable(self, pr_id):
        pull_request = self.repo.get_pull(pr_id)
        return pull_request.mergeable

    """Returns review comments"""
    def get_review_comments(self):
        return self.repo.get_pulls_review_comments()

    "Merges a pr if mergeable"
    def merge_pr(self, pr_id, title, message):
        pull_request = self.repo.get_pull(pr_id)
        if self.get_mergeable(pr_id):
            pull_request.merge(message, title)

    """Checks whether a pr has body text"""
    def check_pr_desc(self, pr_id):
        pull_request = self.repo.get_pull(pr_id)
        if pull_request.body == '':
            pull_request.edit(state=closed)

    """Adds a pr check"""
    def add_pr_check(self, branch, state, url, description, context):
        sha = self.repo.get_git_ref(branch).object.sha
        self.repo.get_commit(sha=sha).create_status(state=state, target_url=url, description=description, context=context)

    """Adds a comment to a pr"""
    def add_comment(self, pr_id, message, commit_id, path, position):
        pull_request = self.repo.get_pull(pr_id)
        pull_request.create_comment(message, commit_id, path, position)

    """Approves a pr"""
    def approve_pr(self, pr_id, commit, body, event, comments):
        pull_request = self.repo.get_pull(pr_id)
        pull_request.create_review(commit=commit, body=body, event=event, comments=comments)

    """Creates a new branch"""
    def new_branch(self, branch_name):
        sha = self.repo.get_git_ref('master').object.sha
        self.repo.create_git_ref(ref='refs/heads/' + branch_name, sha=sha)

    """Deletes a branch"""
    def del_branch(self, branch_name):
        ref = self.repo.get_git_ref(branch_name)
        ref.delete()
