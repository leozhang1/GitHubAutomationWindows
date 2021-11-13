from github import Github
from secrets import Secrets
import os, argparse

# run these in terminal
# python -m venv virtenv (run this only once if you dont have one in the directory already)
# virtenv\Scripts\activate.bat

# to create a public repo: python automate_github.py --name [YourRepoName]
# to create a private repo: python automate_github.py --name [YourRepoName] --private
if __name__ == '__main__':
    pass
    g = Github(Secrets.apiKey)

    # repos = g.search_repositories(query='language:python')
    # for repo in g.get_user().get_repos():
    #     print(repo.name)

    parser = argparse.ArgumentParser()
    parser.add_argument("--name", "-n", type=str,dest="name",required=True)
    parser.add_argument("--private", "-p", dest="isPrivate",action='store_true')
    args = parser.parse_args()
    repoName = args.name
    isPrivate = args.isPrivate

    # create a repo
    user = g.get_user()
    repo = user.create_repo(repoName,private=True if isPrivate else False)

    # creating local repository and connect with the created remote one from above
    try:
        repoPath = Secrets.repoPath
        os.chdir(repoPath)
        os.system(f'mkdir {repoName}')
        os.chdir(f'{repoPath}{repoName}')
        os.system('git init')
        os.system(f'git remote add origin https://github.com/leozhang1/{repoName}.git')
        os.system(f"echo # {repoName} >> README.md")
        os.system('git add .')
        os.system('git commit -m "Initial Commit"')
        os.system('git branch -m main')
        os.system('git push -u origin main')
    except FileExistsError as f:
        print(f)
    except Exception as e:
        print(e)


