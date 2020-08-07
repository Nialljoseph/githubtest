from github import Github


g = Github("c3beda8673b9539d597c37fef28a32cc7e076d42")
repo = g.get_repo("Nialljoseph/GithubTest")
prlist = repo.get_pulls(state='closed', base='master')
for pr in prlist:
    print(pr.number)
