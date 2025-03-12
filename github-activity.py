import argparse
import urllib.request
import json
from colorama import Fore, Style, init

init(autoreset=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='User Activity CLI',
                                     description='CLI-приложение получения информации о последних '
                                                 'действиях пользователя GitHub')

    parser.add_argument("username", type=str, help='ID задачи. (ID of task)')
    username = vars(parser.parse_args()).get('username')

    response = urllib.request.urlopen(f'https://api.github.com/users/{username}/events')
    data = json.loads(response.read())

    for action in data:
        action_type = action.get('type')
        match action_type:
            case "PushEvent":
                print(Fore.GREEN + f"Push {action.get('payload').get('size')} commit(-s) to {action.get('repo').get('name')}")
            case "WatchEvent":
                print(Fore.YELLOW + f"Starred {action.get('repo').get('name')}")
            case "CreateEvent":
                print(Fore.CYAN + f"Add {action.get('payload').get('ref_type')}: {action.get('payload').get('ref')}")
            case "PullRequestEvent":
                print(Fore.MAGENTA + f"PullRequest Type: {action.get('payload').get('action')}")
            case "ForkEvent":
                print(Fore.BLUE + f"Fork: {action.get('payload').get('forkee').get('name')}")
            case "IssueCommentEvent":
                print(Fore.LIGHTWHITE_EX + f"IssueComment: {action.get('payload').get('action')}")
            case "IssuesEvent":
                print(Fore.LIGHTGREEN_EX + f"Issue: {action.get('payload').get('action')}")
            case "PullRequestReviewEvent":
                print(Fore.LIGHTYELLOW_EX + f"PullRequest Review: {action.get('payload').get('action')}")
            case "ReleaseEvent":
                print(Fore.LIGHTCYAN_EX + f"Released {action.get('payload').get('release').get('url').split('/')[5]}")
            case _:
                print(Fore.RED + f"Unknown type: {action_type}")
    
