import argparse
parser = argparse.ArgumentParser()
parser.add_argument("token", type=str, help="GitHub Access Token")
parser.add_argument("organization", type=str, help="GitHub Organization")
parser.add_argument("repo", type=str, help="GitHub Repository")

class GitHub:

    def __init__(self, token, organization, repo):
        self.token = token
        self.org = organization
        self.repo = repo
        g = Github(token)
        repo = g.get_repo(organization + "/" + repo)

    def getOpenPR(self):
        prList = self.repo.get_pulls(state='open', base='master')
        return(prList)
    def getClosedPR(self):
        prList = self.repo.get_pulls(state='closed', base='master')
        return(prList)
    def getOpenPRBranch(self, branch):
        prList = self.repo.get_pulls(state='closed', base=branch)
        return(prList)
    #Start & End in format YYYY-MM-DD
    def getClosedPRDate(self, start, end):
        start = datetime.strptime(start, "%Y-%m-%d")
        end = datetime.strptime(end, "%Y-%m-%d")
        prClosedList = []
        prList = self.repo.get_pulls(state='closed', base='master')
        for pr in prList:
            if pr.closed_at.year >= start.year and pr.closed_at.year <= end.year:
                if pr.closed_at.month >= start.month and pr.closed_at.month <= end.month:
                    if pr.closed_at.day >= start.day and pr.closed_at.day <= end.day:
                        prClosedList.append(pr)
        return(prClosedList)

    def getPRInfo(self, prID):
        pr = repo.get_pull(prID)
        #Wasn't sure how to get dict info so just made it return some info.
        info = [pr.title, pr.body, pr.user.name, pr.user.company, pr.state, pr.commits, pr.base]
        return(info)

    def getApprovers(self, prID):
        pr = repo.get_pull(prID)
        approvers = pr.get_review_requests()
        approveds = []
        for approver in approvers[1]:
            for approved in pr.get_reviews():
                if approver == approved.user:
                    approveds.append(approved)
        return(approveds)

    def getPendingApprovers(self):
        pr = repo.get_pull(prID)
        approvers = pr.get_review_requests()
        approvers = approvers[1]
        approveds = []
        unapproveds = []
        for approver in approvers:
            for approved in pr.get_reviews():
                if approver == approved.user:
                    approveds.append(approved)
        for approver in approvers:
            if approver in approveds:
                pass
            else:
                unapproveds.append(approver)
        return(unapproveds)

    def getMergeable(self, prID):
        pr = repo.get_pull(prID)
        return(pr.mergeable)

    def getReviewComments(self):
        return(repo.get_pulls_review_comments())

    def mergePR(self, prID, title, message):
        pr = repo.get_pull(prID)
        if self.getMergeable(prID):
            pr.merge(message, title)

    def checkPRDesc(self, prID):
        pr = repo.get_pull(prID)
        if pr.body == '':
            pr.edit(state=closed)

    def addPRCheck(self, prID, branch, state, url, description, context):
        pr = repo.get_pull(prID)
        sha = repo.get_git_ref(branch).object.sha
        repo.get_commit(sha=sha).create_status(state=state, target_url=url, description=description, context=context)

    def addComment(self, prID, message, commitID, path, position):
        pr = repo.get_pull(prID)
        pr.create_comment(message, commitID, path, position)

    def approvePR(self, prID, commit, body, event, comments):
        pr = repo.get_pull(prID)
        pr.create_review(commit=commit, body=body, event=event, comments=comments)

    def newBranch(self, branchName):
        sha = repo.get_git_ref('master').object.sha
        repo.create_git_ref(ref='refs/heads/' + branchName, sha=hash)

    def delBranch(self, branchName):
        ref = repo.get_git_ref(branchName)
        ref.delete()

args = parser.parse_args()
GitHub(args.token, args.organization, args.repo)
