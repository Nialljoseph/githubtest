from github import Github

g = Github("c3beda8673b9539d597c37fef28a32cc7e076d42")
repo = g.get_repo("Nialljoseph/GithubTest")
collaborators = repo.get_collaborators()
for collaborator in collaborators:
    print collaborator
prID = input("What is the PR ID: ")
pr = repo.get_pull(prID)
#reviewers = pr.assignees
#for reviewer in reviewers:
    #print reviewer
review_requests = pr.get_review_requests()
for review in review_requests:
    for user in review:
        print(user)
    for team in review:
        print(team)
