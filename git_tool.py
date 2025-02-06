import os, argparse, requests
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("GIT_API_TOKEN")

GITHUB_API_URL = "https://api.github.com"

def get_headers():
    return {"Authorization": f"token: {TOKEN}"}

def get_user_info(username):
    """ Get and display Github user information """

    url = f"{GITHUB_API_URL}/users/{username}"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        data = response.json()
        print(f"\nGithub user: {data['login']}"
              f"\nName: {data.get('name', 'N/A')}"
              f"\nBio: {data.get('bio', 'N/A')}"
              f"\nPublic Repos: {data['public_repos']}")
    else:
        print(f"Error: {response.json().get('message', 'Uknown Error')}")

def list_repos(username):
    """ Fetch and display user repositories """

    url = f"{GITHUB_API_URL}/users/{username}/repos"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        data = response.json()
        if data:
            print(f"\nRepositories of {username}:")
            for repo in data:
                print(f"- {repo['name']} ({repo['html_url']})")
        else:
            print(f"{username} has no public repositories")
    else:
        print(f"Error: {response.josn().get('message', 'Uknown error')}")
    
def get_repo_commits(username, repo, branch="main"):
    """ Fetch and display repo information """
    
    url = f"{GITHUB_API_URL}/repos/{username}/{repo}/commits?sha={branch}"
    response = requests.get(url, headers=get_headers())
    
    if response.status_code == 200:
        data = response.json()
        if data:
            print(f"\n{repo} has '{len(data)}' commits:\n")
            for num, commit in enumerate(data, start=1):
                author = commit['commit']['author']['name']
                message = commit['commit']['message']
                print(f"{num}- {author} : {message}")
        else:
            print(f"{repo} has no commits")
    else:
        print(f"Error: {response.json().get('message', 'Unknown error')}")

def main():

    parser = argparse.ArgumentParser(description="Github CLI tool")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command Get User Info
    user_parser =subparsers.add_parser("user", help="Get Github user details")
    user_parser.add_argument("username", type=str, help="Github username")

    # List all repositories
    repo_parser = subparsers.add_parser("repos", help="List user repositories")
    repo_parser.add_argument("username", type=str, help="Github username")
    
    # 
    commit_parser = subparsers.add_parser("commits", help="Get the number of commits of a repo")
    commit_parser.add_argument("username", type=str, help="Github username")
    commit_parser.add_argument("repo", type=str, help="Name of the repository")

    args = parser.parse_args()
    
    if args.command == "user":
        get_user_info(args.username)
    elif args.command == "repos":
        list_repos(args.username)
    elif args.command == "commits":
        get_repo_commits(args.username, args.repo)
    else:
        parser.print_help

main()