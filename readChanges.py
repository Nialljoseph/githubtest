from github import Github

g = Github("c3beda8673b9539d597c37fef28a32cc7e076d42")
repo = g.get_repo("Nialljoseph/GithubTest")
prID = input("What is the PR ID: ")
pr = repo.get_pull(prID)
files = pr.get_files()
for file in files:
    status = file.status
    if status == "modified":
        print file.filename, "has been modified"
